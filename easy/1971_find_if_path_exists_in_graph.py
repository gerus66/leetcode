# https://leetcode.com/problems/find-if-path-exists-in-graph
# easy
# practice - missed daily
from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        tree = defaultdict(list)
        for [fr, to] in edges:
            tree[fr].append(to)
            tree[to].append(fr)

        to_go, seen = [source], set()
        while to_go:
            node = to_go.pop()
            if node == destination:
                return True
            seen.add(node)
            to_go += [c for c in tree[node] if c not in seen]
        return False
