package lca

type Node struct {
	key   int
	left  *Node
	right *Node
}

func findLeastCommonAncestor(root *Node, n1 int, n2 int) *Node {
	if root == nil {
		return nil
	}

	if root.key == n1 || root.key == n2 {
		return root
	}

	left := findLeastCommonAncestor(root.left, n1, n2)
	right := findLeastCommonAncestor(root.right, n1, n2)

	if left != nil {
		if right != nil {
			return root
		}
		return left
	}

	return right
}