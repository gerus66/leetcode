# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range
# easy
# practice - missed daily
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + int((high % 2) or (low % 2))
    