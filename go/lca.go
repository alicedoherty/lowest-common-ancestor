package lca

type Node struct {
	key   int
	left  *Node
	right *Node
}

func findLeastCommonAncestor(root *Node, n1 int, n2 int) *Node {
	if isNodePresent(root, n1) && isNodePresent(root, n2) {
		return recursiveFindLeastCommonAncestor(root, n1, n2)
	} else {
		return nil
	}
}

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