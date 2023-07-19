# https://leetcode.com/problems/add-digits
# easy
# speed practice of easy tasks
class Solution:
    def addDigits(self, num: int) -> int:
        res, cur = 0, [int(el) for el in str(num)]
        while len(cur) > 1:
            cur = [int(el) for el in str(sum(cur))]
        return cur[0]
    