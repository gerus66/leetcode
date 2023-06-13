# https://leetcode.com/problems/equal-row-and-column-pairs
# medium
# daily
from collections import defaultdict
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = defaultdict(int)
        res = 0
        for row in grid:
            d[tuple(row)] += 1
        for j in range(len(grid)):
            res += d[tuple(grid[i][j] for i in range(len(grid)))]
        return res
