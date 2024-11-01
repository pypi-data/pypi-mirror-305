use std::{collections::HashMap, sync::atomic::AtomicU32};

use anyhow::{ensure, Result};

use crate::api::{GrammarWithLexer, Node, NodeId, NodeProps, RegexSpec, TopLevelGrammar};

#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub struct NodeRef {
    idx: usize,
    grammar_id: u32,
}

pub struct GrammarBuilder {
    pub top_grammar: TopLevelGrammar,
    placeholder: Node,
    strings: HashMap<String, NodeRef>,
    curr_grammar_id: u32,
    nodes: Vec<Node>,
}

impl GrammarBuilder {
    pub fn from_grammar(grammar: TopLevelGrammar) -> (Self, NodeRef) {
        assert!(grammar.grammars.len() == 1);
        let mut builder = Self::new();
        builder.top_grammar = grammar;
        builder.nodes = std::mem::take(&mut builder.top_grammar.grammars[0].nodes);
        builder.next_grammar_id();
        let prev_root = builder.nodes[0].clone();
        builder.nodes[0] = builder.placeholder.clone();
        let prev_root = builder.add_node(prev_root);
        (builder, prev_root)
    }

    pub fn new() -> Self {
        Self {
            top_grammar: TopLevelGrammar {
                grammars: vec![],
                max_tokens: None,
                test_trace: false,
            },
            placeholder: Node::String {
                literal: "__placeholder__: do not use this string in grammars".to_string(),
                props: NodeProps {
                    max_tokens: Some(usize::MAX - 108),
                    capture_name: Some("$$$placeholder$$$".to_string()),
                    ..NodeProps::default()
                },
            },
            strings: HashMap::new(),
            curr_grammar_id: 0,
            nodes: vec![],
        }
    }

    fn shift_nodes(&mut self) {
        if self.top_grammar.grammars.len() == 0 {
            assert!(self.nodes.is_empty(), "nodes added before add_grammar()");
        } else {
            let nodes = std::mem::take(&mut self.nodes);
            assert!(
                nodes.len() > 0,
                "no nodes added before add_grammar() or finalize()"
            );
            self.top_grammar.grammars.last_mut().unwrap().nodes = nodes;
        }
    }

    fn next_grammar_id(&mut self) {
        static COUNTER: AtomicU32 = AtomicU32::new(1);
        self.curr_grammar_id = COUNTER.fetch_add(1, std::sync::atomic::Ordering::Relaxed);
    }

    pub fn add_grammar(&mut self, grammar: GrammarWithLexer) {
        assert!(grammar.nodes.is_empty(), "Grammar already has nodes");
        self.shift_nodes();

        self.next_grammar_id();
        self.top_grammar.grammars.push(grammar);
        self.strings.clear();

        // add root node
        let id = self.placeholder();
        assert!(id.idx == 0);
    }

    fn add_node(&mut self, node: Node) -> NodeRef {
        let r = NodeRef {
            idx: self.nodes.len(),
            grammar_id: self.curr_grammar_id,
        };
        self.nodes.push(node);
        r
    }

    pub fn string(&mut self, s: &str) -> NodeRef {
        if let Some(r) = self.strings.get(s) {
            return *r;
        }
        let r = self.add_node(Node::String {
            literal: s.to_string(),
            props: NodeProps::default(),
        });
        self.strings.insert(s.to_string(), r);
        r
    }

    pub fn special_token(&mut self, name: &str) -> NodeRef {
        self.add_node(Node::SpecialToken {
            token: name.to_string(),
            props: NodeProps::default(),
        })
    }

    pub fn lexeme(&mut self, rx: RegexSpec, json_quoted: bool) -> NodeRef {
        self.add_node(Node::Lexeme {
            rx,
            contextual: None,
            temperature: None,
            json_string: Some(json_quoted),
            json_raw: None,
            json_allowed_escapes: None,
            props: NodeProps::default(),
        })
    }

    fn child_nodes(&mut self, options: &[NodeRef]) -> Vec<NodeId> {
        options
            .iter()
            .map(|e| {
                assert!(e.grammar_id == self.curr_grammar_id);
                NodeId(e.idx)
            })
            .collect()
    }

    pub fn select(&mut self, options: &[NodeRef]) -> NodeRef {
        let ch = self.child_nodes(&options);
        self.add_node(Node::Select {
            among: ch,
            props: NodeProps::default(),
        })
    }

    pub fn join(&mut self, values: &[NodeRef]) -> NodeRef {
        let ch = self.child_nodes(&values);
        self.add_node(Node::Join {
            sequence: ch,
            props: NodeProps::default(),
        })
    }

    pub fn empty(&mut self) -> NodeRef {
        self.string("")
    }

    pub fn optional(&mut self, value: NodeRef) -> NodeRef {
        let empty = self.empty();
        self.select(&[value, empty])
    }

    pub fn zero_or_more(&mut self, elt: NodeRef) -> NodeRef {
        let p = self.placeholder();
        let empty = self.empty();
        let inner = self.select(&[empty, elt]);
        self.set_placeholder(p, inner);
        p
    }

    pub fn placeholder(&mut self) -> NodeRef {
        self.add_node(self.placeholder.clone())
    }

    pub fn is_placeholder(&self, node: NodeRef) -> bool {
        assert!(node.grammar_id == self.curr_grammar_id);
        self.nodes[node.idx] == self.placeholder
    }

    pub fn set_placeholder(&mut self, placeholder: NodeRef, node: NodeRef) {
        let ch = self.child_nodes(&[placeholder, node]); // validate
        if !self.is_placeholder(placeholder) {
            panic!(
                "placeholder already set at {} to {:?}",
                placeholder.idx, self.nodes[placeholder.idx]
            );
        }
        self.nodes[placeholder.idx] = Node::Join {
            sequence: vec![ch[1]],
            props: NodeProps::default(),
        };
    }

    pub fn set_start_node(&mut self, node: NodeRef) {
        self.set_placeholder(
            NodeRef {
                idx: 0,
                grammar_id: self.curr_grammar_id,
            },
            node,
        );
    }

    pub fn finalize(mut self) -> Result<TopLevelGrammar> {
        ensure!(
            self.top_grammar.grammars.len() > 0,
            "No grammars added to the top level grammar"
        );
        self.shift_nodes();
        for grammar in &self.top_grammar.grammars {
            for node in &grammar.nodes {
                ensure!(node != &self.placeholder, "Unresolved placeholder");
            }
        }
        Ok(self.top_grammar.clone())
    }
}
