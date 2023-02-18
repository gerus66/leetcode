# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit
# easy
# biweekly 98
class Solution:
    def minMaxDifference(self, num: int) -> int:
        digits = []
        while num:
            num, d = divmod(num, 10)
            digits.append(d)
        not_9 = [d for d in digits if d != 9]
        turn_to_0, turn_to_9 = digits[-1], not_9[-1] if not_9 else 9
        diff = 0
        for d in reversed(digits):
            diff *= 10
            if d == turn_to_0:
                diff += d
            if d == turn_to_9:
                diff += 9 - d
        return diff
