# https://leetcode.com/problems/possible-bipartition
# medium
# daily
from typing import List
from collections import defaultdict


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        bounds = defaultdict(set)
        for pair in dislikes:
            bounds[pair[0]].add(pair[1])
            bounds[pair[1]].add(pair[0])

        while bounds:
            root, bonds = bounds.popitem()
            current, opposite = bonds, {root}
            to_go, next_to_go = bonds, set()

            while to_go:
                bonds = bounds.pop(to_go.pop(), None)
                if bonds is None:
                    continue
                if current & bonds:
                    return False
                opposite.update(bonds)
                next_to_go.update(bonds)
                if not to_go:
                    to_go, next_to_go = next_to_go, to_go
                    current, opposite = opposite, current

        return True
