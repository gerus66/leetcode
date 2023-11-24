# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array
# medium
# daily mock interview
class Solution:
    @staticmethod
    def ar_sum(n: int) -> int:
        return n * (n + 1) // 2

    def calc_sum(self, n: int, index: int, val: int) -> int:
        left_side = self.ar_sum(val) - self.ar_sum(max(val - (index + 1), 0))
        left_side += max((index + 1) - val, 0)
        right_side = self.ar_sum(val) - self.ar_sum(max(val - (n - index), 0))
        right_side += max((n - index) - val, 0)
        return left_side + right_side - val

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right, check = 0, maxSum + 1, 0
        while left != right:
            check = (left + right) // 2
            cur_sum = self.calc_sum(n, index, check)
            if cur_sum == maxSum:
                return check
            if cur_sum > maxSum:
                right = check
            else:
                left = check + 1
        return left - 1
