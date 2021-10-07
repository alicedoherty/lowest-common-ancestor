import unittest
# import lca

from lca import findLCA, Node

# Cases we want to test:
#  - standard looking tree
#  - tree where LCA is one of the nodes 
#  - tree that's straight line
#  - test both the same number
#  - single node tree?
#  - null tree?


class TestLCA(unittest.TestCase):
    #          1
    #        /   \
    #      2       3
    #    /   \   /   \
    #   4     5 6     7

    def test_basic_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        lca1 = lca.findLCA(root, 4, 5)
        lca2 = lca.findLCA(root, 5, 3)
        self.assertEqual(lca1, 2)
        self.assertEqual(lca2, 1)


    def test_two(self):
        pass
    

if __name__ == '__main__':
    unittest.main()