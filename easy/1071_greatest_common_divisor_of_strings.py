# https://leetcode.com/problems/greatest-common-divisor-of-strings
# easy
# daily
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        small, big = (str1, str2) if len(str1) < len(str2) else (str2, str1)
        while small:
            if big[:len(small)] != small:
                return ""
            big = big[len(small):]
            if len(big) < len(small):
                small, big = big, small
        return big
    