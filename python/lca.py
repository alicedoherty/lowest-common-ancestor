# Python program to find LCA of n1 and n2 using one traversal of Binary tree.
# Code is adapted from GeeksForGeeks.org

class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# TODO add function to check n1 and n2 are present in binary tree

def findLCA(root, n1, n2):
    """
    Returns a point to the LCA of two given nodes, n1 and n2.
    If one Node is an ancestor of the other, then the parent node is the LCA.
    Assumes that n1 and n2 are in the binary tree.

    Parameters:
        root - the root Node of the binary tree
        n1 - the first Node
        n2 - the second Node
    """

    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root

    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca