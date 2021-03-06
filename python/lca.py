# Python program to find LCA of two nodes of a directed acyclic graph.
# Assumes that each node has a unique key.

import sys


class Graph:
    # Initialise Graph with empty graph (dict)
    def __init__(self):
        self.graph = {}

    # Add a node to the graph
    def add_node(self, node, graph={}):
        if not graph:
            graph = self.graph

        if node in graph:
            return False

        # Initialise a list to contain the nodes edges
        graph[node] = []

    # Add an edge to the graph (n1 = initial node, n2 = terminal node)
    # i.e direction = n1 -> n2
    def add_edge(self, n1, n2, graph={}):
        if not graph:
            graph = self.graph

        # Can only add edge if both the nodes are in the graph
        if n1 in graph and n2 in graph:
            graph[n1].append(n2)
            return True

        return False


def findLCA(graph, n1, n2):
    """
    If both n1 and n2 are in the graph and the graph is acyclic finds the LCA using DFS,
    otherwise returns None.

    Parameters:
        graph - the graph
        n1 - the first Node
        n2 - the second Node
    """

    if not isAcyclic(graph):
        return None

    global n1_list
    global n2_list
    n1_list = []
    n2_list = []

    for node in graph:
        dfs([node], graph, node, 1, n1)
        dfs([node], graph, node, 2, n2)

    min_dist = sys.maxsize
    for x in n1_list:
        for y in n2_list:
            dist = 0
            for i, nX in enumerate(reversed(x)):
                dist = i
                for nY in reversed(y):
                    if nX == nY and dist < min_dist:
                        # LCA is node with shortest distance
                        lca = nY
                        min_dist = dist
                        return lca

                    dist += 1

    return None


# Depth First Search for a node
def dfs(node_list, graph, node, i, terminal_node):
    if node == terminal_node:
        if i == 1:
            n1_list.append(node_list[:])
        elif i == 2:
            n2_list.append(node_list[:])
        return True

    if not graph[node]:
        return True

    else:
        for x in graph[node]:
            node_list.append(x)
            dfs(node_list, graph, x, i, terminal_node)
            node_list.remove(x)
        return True


# Returns True is the provided graph is acyclic
def isAcyclic(graph):
    for node in graph:
        if not isAcyclicRecursive([node], graph, node):
            return False

    return True


def isAcyclicRecursive(node_list, graph, node):
    if not graph[node]:
        return True
    else:
        for x in graph[node]:
            if x not in node_list:
                node_list.append(x)
                if not isAcyclicRecursive(node_list, graph, x):
                    return False
                node_list.remove(x)
            else:
                return False
        return True
