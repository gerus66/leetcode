# https://leetcode.com/problems/check-if-point-is-reachable
# hard
# practice missed contest - biweekly 96
import math


class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        gcd = math.gcd(targetX, targetY)
        return gcd and gcd & (gcd - 1) == 0
