# https://leetcode.com/problems/zigzag-conversion
# medium
# daily
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ""
        for r in range(numRows):
            for i in range(r, len(s), 2*numRows-2 or 1):
                ans += s[i]
                if r and numRows-r-1 and i+2*(numRows-1-r) < len(s):
                    ans += s[i+2*(numRows-1-r)]
        return ans
    