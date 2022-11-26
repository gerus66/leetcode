# https://leetcode.com/problems/minimum-cuts-to-divide-a-circle
# easy
# biweekly contest 92

class Solution:
    def numberOfCuts(self, n: int) -> int:
        return 0 if n == 1 else (n if n % 2 else int(n / 2))
