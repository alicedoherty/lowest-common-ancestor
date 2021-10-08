// Go program to find LCA of two nodes of a binary tree.
// Assumes that each node has a unique key.

package lca

type Node struct {
	key   int
	left  *Node
	right *Node
}


// If both n1 and n2 are in the binary tree calls recursiveFindLCA() and returns the LCA,
// otherwise returns None.
func findLeastCommonAncestor(root *Node, n1 int, n2 int) *Node {
	if isNodePresent(root, n1) && isNodePresent(root, n2) {
		return recursiveFindLeastCommonAncestor(root, n1, n2)
	} else {
		return nil
	}
}

// Returns a pointer to the LCA of two given nodes, n1 and n2.
// If one Node is an ancestor of the other, then the parent node is the LCA.
func recursiveFindLeastCommonAncestor(root *Node, n1 int, n2 int) *Node {
	if root == nil {
		return nil
	}

	if root.key == n1 || root.key == n2 {
		return root
	}

	left := recursiveFindLeastCommonAncestor(root.left, n1, n2)
	right := recursiveFindLeastCommonAncestor(root.right, n1, n2)

	if left != nil {
		if right != nil {
			return root
		}
		return left
	}

	return right
}

// Checks if a key is present in a given binary tree.
func isNodePresent(root *Node, key int) bool {
	if root == nil {
		return false
	}

	if root.key == key {
		return true
	}
	
	left := isNodePresent(root.left, key)

	if left {
		return true
	}

	right := isNodePresent(root.right, key)

	return right
}