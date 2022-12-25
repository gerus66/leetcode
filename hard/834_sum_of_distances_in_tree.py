# https://leetcode.com/problems/sum-of-distances-in-tree
# hard
# training - missed daily
from typing import List


class Solution:
    def __init__(self):
        self.distances = []
        self.base = 0
        self.last_key = 0

    @staticmethod
    def find_end_of_tree(nodes, start):
        current, parent = start, start
        while len(nodes[current][1]) > 1:
            for child in nodes[current][1]:
                if child != parent:
                    parent, current = current, child
                    break
        return current

    def do_the_job(self, nodes, key):
        if not nodes[key][1]:
            return

        self.base += nodes[key][0]
        self.last_key = key
        next_key = nodes[key][1].pop()  # always 1 bond
        nodes[key][2].append(next_key)
        nodes[next_key][1].remove(key)
        nodes[next_key][2].append(key)
        if not nodes[next_key][1]:
            return

        nodes[next_key][0] += nodes[key][0]
        if len(nodes[next_key][1]) == 1:  # do it besides order
            return next_key

        return self.find_end_of_tree(nodes, next_key)

    def count_nodes(self, nodes):
        end_of_tree = self.find_end_of_tree(nodes, 0)

        while end_of_tree is not None:
            end_of_tree = self.do_the_job(nodes, end_of_tree)

    def count_distances(self, nodes, n):
        distances = [self.base]*n
        to_count = [(self.last_key, 0)]
        while to_count:
            key, accumulated = to_count.pop()
            if nodes.get(key, None) is None:
                continue
            node = nodes.pop(key)

            accumulated += n - 2*node[0]
            distances[key] += accumulated
            to_count.extend([(nd, accumulated) for nd in node[2] ])
        return distances

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = {}
        for edge in edges:
            for i in range(2):
                if edge[i] not in nodes:
                    nodes[edge[i]] = [1, [], []]
                nodes[edge[i]][1].append(edge[i-1])
        if not nodes:
            return [0]

        self.count_nodes(nodes)
        return self.count_distances(nodes, n)
