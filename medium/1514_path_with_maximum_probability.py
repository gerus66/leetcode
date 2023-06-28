# https://leetcode.com/problems/path-with-maximum-probability
# medium
# daily
from collections import defaultdict
import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, nodes in enumerate(edges):
            graph[nodes[0]].append((succProb[i], nodes[1]))
            graph[nodes[1]].append((succProb[i], nodes[0]))
        # print(graph)
        been_here = dict()
        h = [(-1, start)]
        while h:
            prob, cur = heapq.heappop(h)
            # print(f'node {cur}, prob = {-prob}')
            if cur == end:
                return -prob
            if cur not in graph:
                continue
            if cur in been_here and been_here[cur] >= -prob:
                continue
            been_here[cur] = -prob
            nexts = graph[cur]
            for next_prob, next_node in nexts:
                heapq.heappush(h, (prob * next_prob, next_node))
        return 0
