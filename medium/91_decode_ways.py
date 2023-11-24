# https://leetcode.com/problems/decode-ways
# medium
# Uber interview prep
class Solution:
    def numDecodings(self, s: str) -> int:
        prev = (1, int(not (s[0] == '0')))
        for i in range(1, len(s)):
            count_groups = 0
            if s[i] != '0':
                count_groups += prev[-1]
            if 9 < int(s[i-1:i+1]) < 27:
                count_groups += prev[-2]
            prev = (prev[-1], count_groups)
        return prev[-1]
