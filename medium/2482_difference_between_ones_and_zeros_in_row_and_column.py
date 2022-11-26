# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column
# medium
# biweekly contest 92 - virtual
from typing import List


class Solution:
    row_sums = []
    col_sums = []

    def count_sums(self, elem, i_row, i_col):
        if elem:
            self.row_sums[i_row] += 1
            self.col_sums[i_col] += 1
        else:
            self.row_sums[i_row] -= 1
            self.col_sums[i_col] -= 1

    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        diff = [[0 for _ in grid[0]] for _ in grid]
        self.row_sums = [0 for _ in grid]
        self.col_sums = [0 for _ in grid[0]]
        for i_row, row in enumerate(grid):
            for i_col, elem in enumerate(row):
                self.count_sums(elem, i_row, i_col)
        for i_row, row in enumerate(diff):
            for i_col, elem in enumerate(row):
                diff[i_row][i_col] = self.row_sums[i_row] + self.col_sums[i_col]
        return diff
