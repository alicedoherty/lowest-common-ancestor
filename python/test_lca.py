import unittest
import lca


class TestLCA(unittest.TestCase):

    #
    # First section of tests cover original binary tree cases.
    #

    def test_basic_tree(self):
        # Test basic LCA queries with below binary tree.
        #
        #          1
        #        /   \
        #      2       3
        #    /   \   /   \
        #   4     5 6     7

        tree = lca.Graph()
        tree.add_node(1)
        tree.add_node(2)
        tree.add_node(3)
        tree.add_node(4)
        tree.add_node(5)
        tree.add_node(6)
        tree.add_node(7)

        tree.add_edge(1, 2)
        tree.add_edge(1, 3)
        tree.add_edge(2, 4)
        tree.add_edge(2, 5)
        tree.add_edge(3, 6)
        tree.add_edge(3, 7)

        result1 = lca.findLCA(tree.graph, 4, 5)
        result2 = lca.findLCA(tree.graph, 5, 3)

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

        tree = lca.Graph()
        tree.add_node(1)
        tree.add_node(2)
        tree.add_node(3)
        tree.add_node(4)

        tree.add_edge(1, 2)
        tree.add_edge(2, 3)
        tree.add_edge(3, 4)

        result = lca.findLCA(tree.graph, 3, 2)
        self.assertEqual(result, 2)

    def test_node_is_lca(self):
        # Test when one of the provided nodes is the LCA.
        # e.g LCA of 4 and 2 is 2
        #
        #          1
        #        /   \
        #      2       3
        #    /   \
        #   4     5

        tree = lca.Graph()
        tree.add_node(1)
        tree.add_node(2)
        tree.add_node(3)
        tree.add_node(4)
        tree.add_node(5)

        tree.add_edge(1, 2)
        tree.add_edge(1, 3)
        tree.add_edge(2, 4)
        tree.add_edge(2, 5)

        result = lca.findLCA(tree.graph, 4, 2)
        self.assertEqual(result, 2)

    def test_node_not_included(self):
        # Test when provided node is not in the binary tree.
        #
        #          1
        #        /   \
        #      2       3
        #    /   \
        #   4     5

        tree = lca.Graph()
        tree.add_node(1)
        tree.add_node(2)
        tree.add_node(3)
        tree.add_node(4)
        tree.add_node(5)

        tree.add_edge(1, 2)
        tree.add_edge(1, 3)
        tree.add_edge(2, 4)
        tree.add_edge(2, 5)

        result = lca.findLCA(tree.graph, 0, 2)
        self.assertEqual(result, None)

    def test_null_tree(self):
        # Test when there is no binary tree (root is None).

        tree = lca.Graph()
        result = lca.findLCA(tree.graph, 1, 2)
        self.assertEqual(result, None)

    #
    # Second second of tests cover DAG cases.
    #

    def test_classic_dag(self):
        # Test with basic DAG.
        # Picture: https://upload.wikimedia.org/wikipedia/commons/f/fe/Tred-G.svg

        dag = lca.Graph()
        dag.add_node(1)
        dag.add_node(2)
        dag.add_node(3)
        dag.add_node(4)
        dag.add_node(5)

        dag.add_edge(1, 2)
        dag.add_edge(1, 3)
        dag.add_edge(1, 4)
        dag.add_edge(1, 5)
        dag.add_edge(2, 4)
        dag.add_edge(3, 4)
        dag.add_edge(3, 5)
        dag.add_edge(4, 5)

        result = lca.findLCA(dag.graph, 2, 3)
        self.assertEqual(result, 1)

    def test_node_is_lca_dag(self):
        # Test when one of the provided nodes is the LCA.
        # Picture: https://upload.wikimedia.org/wikipedia/commons/f/fe/Tred-G.svg

        dag = lca.Graph()
        dag.add_node(1)
        dag.add_node(2)
        dag.add_node(3)
        dag.add_node(4)
        dag.add_node(5)

        dag.add_edge(1, 2)
        dag.add_edge(1, 3)
        dag.add_edge(1, 4)
        dag.add_edge(1, 5)
        dag.add_edge(2, 4)
        dag.add_edge(3, 4)
        dag.add_edge(3, 5)
        dag.add_edge(4, 5)

        result = lca.findLCA(dag.graph, 4, 5)
        self.assertEqual(result, 4)

    def test_node_not_included_dag(self):
        # Test when node is not included in DAG.
        #
        #         1
        #       / | \
        #      2  3  4

        dag = lca.Graph()
        dag.add_node(1)
        dag.add_node(2)
        dag.add_node(3)
        dag.add_node(4)

        dag.add_edge(1, 2)
        dag.add_edge(1, 3)
        dag.add_edge(1, 4)

        result = lca.findLCA(dag.graph, 4, 5)
        self.assertEqual(result, None)

    def test_cyclic_dag(self):
        # Test when the directed graph is cyclic.
        # Should return None as by definition a DAG is acyclic.
        #
        #   1 → 2
        #   ↑   ↓
        #   4 ← 3

        dag = lca.Graph()
        dag.add_node(1)
        dag.add_node(2)
        dag.add_node(3)
        dag.add_node(4)

        dag.add_edge(1, 2)
        dag.add_edge(2, 3)
        dag.add_edge(3, 4)
        dag.add_edge(4, 1)

        result = lca.findLCA(dag.graph, 2, 3)
        self.assertEqual(result, None)

    def test_diff_directions_dag(self):
        # Test with a DAG with edges in different directions.

        dag = lca.Graph()
        dag.add_node(1)
        dag.add_node(2)
        dag.add_node(3)
        dag.add_node(4)
        dag.add_node(5)
        dag.add_node(6)

        dag.add_edge(1, 2)
        dag.add_edge(1, 3)
        dag.add_edge(3, 5)
        dag.add_edge(4, 2)
        dag.add_edge(5, 2)
        dag.add_edge(6, 4)
        dag.add_edge(6, 5)

        result = lca.findLCA(dag.graph, 4, 5)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
