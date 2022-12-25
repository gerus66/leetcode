# https://leetcode.com/problems/minimum-falling-path-sum
# medium
# training - missed daily
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        mins = matrix[0]
        for row in matrix[1:]:
            prev = mins[0]
            for i, elem in enumerate(row):
                nxt = mins[i+1] if i < len(matrix) - 1 else mins[-1]
                prev, mins[i] = mins[i], min(prev, mins[i], nxt) + elem
        return min(mins)
