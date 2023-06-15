# https://leetcode.com/problems/design-graph-with-shortest-path-calculator
# hard
# biweekly 102 - virtual
from typing import List
from collections import defaultdict
import heapq
import math


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.gr_dict = defaultdict(list)
        for fr, to, cost in edges:
            self.gr_dict[fr].append((cost, to))

    def addEdge(self, edge: List[int]) -> None:
        self.gr_dict[edge[0]].append((edge[2], edge[1]))

    def shortestPath(self, node1: int, node2: int) -> int:
        h = [(0, node1)]
        seen_dict = {node1: 0}
        while h:
            cur_cost, cur_node = heapq.heappop(h)
            if cur_node == node2:
                return cur_cost
            for next_cost, next_node in self.gr_dict[cur_node]:
                if cur_cost + next_cost < seen_dict.get(next_node, math.inf):
                    heapq.heappush(h, (cur_cost + next_cost, next_node))
                    seen_dict[next_node] = cur_cost + next_cost
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
