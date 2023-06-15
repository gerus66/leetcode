# https://leetcode.com/problems/find-the-width-of-columns-of-a-grid
# easy
# biweekly 102 - virtual
from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = [1 for _ in range(len(grid[0]))]
        for row in grid:
            for i, el in enumerate(row):
                if (tmp := len(str(el))) > ans[i]:
                    ans[i] = tmp
        return ans
