# https://leetcode.com/problems/find-closest-node-to-given-two-nodes
# medium
# daily
from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def update_dict(start, d, edges):
        seen = set()
        node, path = start, 0
        while node != -1 and node not in seen:
            seen.add(node)
            d[node].append(path)
            path += 1
            node = edges[node]

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        d = defaultdict(list)
        self.update_dict(node1, d, edges)
        self.update_dict(node2, d, edges)
        d = {k: max(v) for k, v in d.items() if len(v) > 1}
        if not d:
            return -1
        min_path = min(d.values())
        d = {k: v for k, v in d.items() if v == min_path}
        return min(d.keys())
