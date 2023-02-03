# https://leetcode.com/problems/climbing-stairs
# easy
# practice - missed daily
class Solution:
    def climbStairs(self, n: int) -> int:
        end_by_1, end_by_2 = 1, 0
        for i in range(2, n+1):
            end_by_1, end_by_2 = end_by_1 + end_by_2, end_by_1
        return end_by_1 + end_by_2
    