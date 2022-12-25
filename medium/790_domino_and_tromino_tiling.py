# https://leetcode.com/problems/domino-and-tromino-tiling
# medium
# training - missed daily
class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3:
            return n
        minus_3_sum, minus_2, minus_1 = 0, 1, 2
        tilings = 0
        if n == 2:
            return tilings
        for i in range(3, n+1):
            tilings = minus_3_sum * 2 + minus_2 + minus_1 + 2
            minus_3_sum += minus_2
            minus_2, minus_1 = minus_1, tilings
        return tilings % (10**9 + 7)
    