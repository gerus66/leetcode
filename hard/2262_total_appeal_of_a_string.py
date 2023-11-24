# https://leetcode.com/problems/total-appeal-of-a-string
# hard
# daily mock interview
class Solution:
    def appealSum(self, s: str) -> int:
        last_seen = dict()
        prev, rlt = 0, 0
        for i, ch in enumerate(s):
            prev += 1 + (i - last_seen.get(ch, -1) - 1)
            rlt += prev
            last_seen[ch] = i
        return rlt
