# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
# easy
# daily
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle)+1):
            j = 0
            while haystack[i] == needle[j]:
                i, j = i + 1, j + 1
                if j == len(needle):
                    return i - len(needle)
        return -1
    