import numpy as np


class Node:
    def __init__(self, value):
        self.value = value
        self.color = 'White'
        self.d = 0
        self.f = 0
        self.pi = []

    def get_parents(self):
        return self.pi


class BayesianNetwork:
    def __init__(self, n):
        self.N = n
        self.adjacency_matrix = np.zeros((n, n))
        self.nodes = []
        for i in range(n):
            self.nodes.append(Node(i))

    def set_matrix(self, new_matrix):
        self.adjacency_matrix = new_matrix
        for i in range(self.N):
            for j in range(self.N):
                if self.adjacency_matrix[j, i] == 1:
                    self.nodes[i].pi.append(j)

    def get_nodes(self):
        return self.nodes
