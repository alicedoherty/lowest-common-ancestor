package lca

import (
    "testing"
)

// Add comments

func TestBasicTree(t *testing.T) {
    // Test basic LCA queries with below binary tree.
    //         1
    //       /   \
    //     2       3
    //   /   \   /   \
    //  4     5 6     7

    root := Node{1, nil, nil}
	root.left = &Node{2, nil, nil}
	root.right = &Node{3, nil, nil}
    root.left.left = &Node{4, nil, nil}
    root.left.right = &Node{5, nil, nil}
    root.right.left = &Node{6, nil, nil}
    root.right.right = &Node{7, nil, nil}

    tables := []struct {
        n1 int
        n2 int
        expectedLCA int
    }{
        {4, 5, 2},
        {4, 3, 1},
        {2, 3, 1},
        {2, 7, 1},
    }

    for _, table := range tables {
        lca := findLeastCommonAncestor(&root, table.n1, table.n2).key

        if lca != table.expectedLCA {
            t.Errorf("LCA of %d and %d is incorrect, got %d, want %d.", table.n1, table.n2, lca, table.expectedLCA)
        }
    }
}

func TestStraightTree(t *testing.T) {
    // Test funky looking binary tree.
    //
    //  1
    //   \
    //    2
    //     \
    //      3
    //       \
    //        4

    root := Node{1, nil, nil}
	root.right = &Node{2, nil, nil}
	root.right.right = &Node{3, nil, nil}
    root.right.right.right = &Node{4, nil, nil}

    lca := findLeastCommonAncestor(&root, 4, 3).key

    if lca != 3 {
        t.Errorf("LCA is incorrect, got %d, want %d", lca, 3)
    }
}

func TestNodeIsLCA(t *testing.T) {
    // Test when one of the provided nodes is the LCA.
    // e.g LCA of 4 and 2 is 2
    //
    //          1
    //        /   \
    //      2       3
    //    /   \
    //   4     5

    root := Node{1, nil, nil}
	root.left = &Node{2, nil, nil}
	root.right = &Node{3, nil, nil}
    root.left.left = &Node{4, nil, nil}
    root.left.right = &Node{5, nil, nil}

    lca := findLeastCommonAncestor(&root, 4, 2).key

    if lca != 2 {
        t.Errorf("LCA is incorrect, got %d, want %d", lca, 2)
    }
}

func TestNodeNotIncluded(t *testing.T) {
    // Test whe provided node is not in the binary tree.
    //
    //          1
    //        /   \
    //      2       3
    //    /   \
    //   4     5

    root := Node{1, nil, nil}
	root.left = &Node{2, nil, nil}
	root.right = &Node{3, nil, nil}
    root.left.left = &Node{4, nil, nil}
    root.left.right = &Node{5, nil, nil}

    lca := findLeastCommonAncestor(&root, 0, 2)

    if lca != nil {
        t.Errorf("LCA is incorrect, should return nil if node(s) not present in tree")
    }
}

func TestNullTree(t *testing.T) {
    // Test when there is no binary tree (root is None).

    var root *Node = nil 

    lca := findLeastCommonAncestor(root, 1, 2)

    if lca != nil {
        t.Errorf("LCA is incorrect, empty tree should return nil")
    }
}