package main

import (
    "testing"
    "regexp"
)

// Add comments

func TestBasicTree(t *testing.T) {
    root := Node{1, nil, nil}
	root.left = &Node{2, nil, nil}
	root.right = &Node{3, nil, nil}
    root.left.left = &Node{4, nil, nil}
    root.left.right = &Node{5, nil, nil}
    root.right.left = &Node{6, nil, nil}
    root.right.right = &Node{7, nil, nil}

    lca := findLeastCommonAncestor(&root, 5, 3)
    if lca != 1 {
        t.Errorf("LCA is incorrect, got %d, want %d.", lca, 1)
    }
}