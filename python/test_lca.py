import unittest
import lca


class TestLCA(unittest.TestCase):

    # def test_basic_tree(self):
    #     # Test basic LCA queries with below binary tree.
    #     #
    #     #          1
    #     #        /   \
    #     #      2       3
    #     #    /   \   /   \
    #     #   4     5 6     7

    #     root = lca.Node(1)
    #     root.left = lca.Node(2)
    #     root.right = lca.Node(3)
    #     root.left.left = lca.Node(4)
    #     root.left.right = lca.Node(5)
    #     root.right.left = lca.Node(6)
    #     root.right.right = lca.Node(7)

    #     result1 = lca.findLCA(root, 4, 5).key
    #     result2 = lca.findLCA(root, 5, 3).key

    #     self.assertEqual(result1, 2)
    #     self.assertEqual(result2, 1)

    # def test_straight_tree(self):
    #     # Test funky looking binary tree.
    #     #
    #     #  1
    #     #   \
    #     #    2
    #     #     \
    #     #      3
    #     #       \
    #     #        4

    #     root = lca.Node(1)
    #     root.right = lca.Node(2)
    #     root.right.right = lca.Node(3)
    #     root.right.right.right = lca.Node(4)

    #     result = lca.findLCA(root, 4, 3).key
    #     self.assertEqual(result, 3)

    # def test_node_is_lca(self):
    #     # Test when one of the provided nodes is the LCA.
    #     # e.g LCA of 4 and 2 is 2
    #     #
    #     #          1
    #     #        /   \
    #     #      2       3
    #     #    /   \
    #     #   4     5

    #     root = lca.Node(1)
    #     root.left = lca.Node(2)
    #     root.right = lca.Node(3)
    #     root.left.left = lca.Node(4)
    #     root.left.right = lca.Node(5)

    #     result = lca.findLCA(root, 4, 2).key
    #     self.assertEqual(result, 2)

    # def test_node_not_included(self):
    #     # Test when provided node is not in the binary tree.
    #     #
    #     #          1
    #     #        /   \
    #     #      2       3
    #     #    /   \
    #     #   4     5

    #     root = lca.Node(1)
    #     root.left = lca.Node(2)
    #     root.right = lca.Node(3)
    #     root.left.left = lca.Node(4)
    #     root.left.right = lca.Node(5)

    #     result = lca.findLCA(root, 0, 2)
    #     self.assertEqual(result, None)

    # def test_null_tree(self):
    #     # Test when there is no binary tree (root is None).

    #     root = None
    #     result = lca.findLCA(root, 1, 2)
    #     self.assertEqual(result, None)

    def test_classic_dag(self):
        # Test with basic DAG.
        # Picture: https://upload.wikimedia.org/wikipedia/commons/f/fe/Tred-G.svg

        root = lca.Node(1)
        n2 = lca.Node(2)
        n3 = lca.Node(3)
        n4 = lca.Node(4)
        n5 = lca.Node(5)

        root.children = [n2, n3, n4, n5]
        n2.parents = [root]
        n2.children = [n4]
        n3.parents = [root]
        n3.children = [n4, n5]
        n4.parents = [root, n2, n3]
        n4.children = [n5]
        n5.parents = [root, n3, n4]

        result = lca.recursiveFindLCA(root, n4, n5)
        self.assertEqual(result, 3)

    def test_node_not_included_dag(self):
        # Test when node is not included in DAG.
        #         1
        #       / | \
        #      2  3  4

        root = lca.Node(1)
        n2 = lca.Node(2)
        n3 = lca.Node(3)
        n4 = lca.Node(4)

        # Defining the n5 (to avoid NameError), but it is not
        # included in the DAG
        n5 = lca.Node(-1)

        root.children = [n2, n3, n4]
        n2.parents = [root]
        n3.parents = [root]
        n4.parents = [root]

        result = lca.recursiveFindLCA(root, n4, n5)
        self.assertEqual(result, None)

    def test_node_is_lca_dag(self):
        # Test when one of the provided nodes is the LCA.
        # e.g LCA of 5 and 3 is 3
        #
        #         1
        #      /  |  \
        #     2   3   4
        #        /|\
        #       5 6 7

        root = lca.Node(1)
        n2 = lca.Node(2)
        n3 = lca.Node(3)
        n4 = lca.Node(4)
        n5 = lca.Node(5)
        n6 = lca.Node(6)
        n7 = lca.Node(7)

        root.children = [n2, n3, n4]
        n2.parents = [root]
        n3.parents = [root]
        n3.children = [n5, n6, n7]
        n4.parents = [root]
        n5.parents = [n3]
        n6.parents = [n3]
        n7.parents = [n3]

        result = lca.recursiveFindLCA(root, n5, n3)
        self.assertEqual(result, 3)

    def test_cyclic_dag(self):
        # Test when the directed graph is cyclic.
        # Should return None as by definition a DAG is acyclic.
        #
        #   1 → 2
        #   ↑   ↓
        #   4 ← 3

        root = lca.Node(1)
        n2 = lca.Node(2)
        n3 = lca.Node(3)
        n4 = lca.Node(4)

        root.parents = [n4]
        root.children = [n2]
        n2.parents = [root]
        n2.children = [n3]
        n3.parents = [n2]
        n3.children = [n4]
        n4.parents = [n3]
        n4.children = [root]

        result = lca.recursiveFindLCA(root, n2, n3)
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
