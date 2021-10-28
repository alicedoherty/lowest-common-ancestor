import unittest
import lca


class TestLCA(unittest.TestCase):

    def test_basic_tree(self):
        # Test basic LCA queries with below binary tree.
        #
        #          1
        #        /   \
        #      2       3
        #    /   \   /   \
        #   4     5 6     7

        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)

        result1 = lca.findLCA(root, 4, 5).key
        result2 = lca.findLCA(root, 5, 3).key

        self.assertEqual(result1, 2)
        self.assertEqual(result2, 1)

    def test_straight_tree(self):
        # Test funky looking binary tree.
        #
        #  1
        #   \
        #    2
        #     \
        #      3
        #       \
        #        4

        root = lca.Node(1)
        root.right = lca.Node(2)
        root.right.right = lca.Node(3)
        root.right.right.right = lca.Node(4)

        result = lca.findLCA(root, 4, 3).key
        self.assertEqual(result, 3)

    def test_node_is_lca(self):
        # Test when one of the provided nodes is the LCA.
        # e.g LCA of 4 and 2 is 2
        #
        #          1
        #        /   \
        #      2       3
        #    /   \
        #   4     5

        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)

        result = lca.findLCA(root, 4, 2).key
        self.assertEqual(result, 2)

    def test_node_not_included(self):
        # Test when provided node is not in the binary tree.
        #
        #          1
        #        /   \
        #      2       3
        #    /   \
        #   4     5

        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)

        result = lca.findLCA(root, 0, 2)
        self.assertEqual(result, None)

    def test_null_tree(self):
        # Test when there is no binary tree (root is None).

        root = None
        result = lca.findLCA(root, 1, 2)
        self.assertEqual(result, None)

    def test_basic_dag(self):
        # Can't write DAG test as there is no DAG data structure

if __name__ == '__main__':
    unittest.main()
