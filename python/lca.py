# Python program to find LCA of two nodes of a binary tree.
# Code is adapted from GeeksForGeeks.org
# Assumes that each node has a unique key.

class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def findLCA(root, n1, n2):
    """
    If both n1 and n2 are in the binary tree calls recursiveFindLCA() and returns the LCA,
    otherwise returns None.

    Parameters:
        root - the root Node of the binary tree
        n1 - the first Node
        n2 - the second Node
    """

    if isNodePresent(root, n1) and isNodePresent(root, n2):
        return recursiveFindLCA(root, n1, n2)
    else:
        return None


def recursiveFindLCA(root, n1, n2):
    """
    Returns a pointer to the LCA of two given nodes, n1 and n2.
    If one Node is an ancestor of the other, then the parent node is the LCA.

    Parameters:
        root - the root Node of the binary tree
        n1 - the first Node
        n2 - the second Node
    """

    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root

    left_lca = recursiveFindLCA(root.left, n1, n2)
    right_lca = recursiveFindLCA(root.right, n1, n2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca


def isNodePresent(root, key):
    """
    Checks if a key is present in a given binary tree.

    Parameters:
        root - the root Node of the binary tree
        key - the value of the Node to check
    """

    if root is None:
        return False

    if root.key == key:
        return True

    left = isNodePresent(root.left, key)

    if left:
        return True

    right = isNodePresent(root.right, key)

    return right