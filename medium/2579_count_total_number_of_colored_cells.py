# https://leetcode.com/problems/count-total-number-of-colored-cells
# medium
# biweekly contest 99
class Solution:
    def coloredCells(self, n: int) -> int:
        count = 1
        for i in range(2, n + 1):
            count += i * 4 - 4
        return count
