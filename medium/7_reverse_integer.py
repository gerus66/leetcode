# https://leetcode.com/problems/reverse-integer
# medium
# just practice
class Solution:
    def reverse(self, x: int) -> int:
        res, src, dec = 0, abs(x), 0
        while src:
            if res > 214748364 or (res == 214748364 and (src%10>=8 or x<0 and src%10>8)):
                return 0
            res, src, dec = res * 10 + src % 10, src // 10, dec + 1
        return res if x > 0 else -res
    