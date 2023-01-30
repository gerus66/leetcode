# https://leetcode.com/problems/n-th-tribonacci-number
# easy
# daily
class Solution:
    def tribonacci(self, n: int) -> int:
        prev = [0, 1, 1]
        for _ in range(n//3*3):
            prev = [prev[1], prev[2], sum(prev)]
        return prev[n%3]
    