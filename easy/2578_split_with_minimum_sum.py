# https://leetcode.com/problems/split-with-minimum-sum
# easy
# biweekly contest 99
class Solution:
    def splitNum(self, num: int) -> int:
        digits = [i for i in str(num)]
        digits.sort()
        num1 = digits[::2]
        num2 = digits[1::2]
        return int(''.join(num1)) + int(''.join(num2))
