# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string
# easy
# speed practice of easy tasks
class Solution:
    def minOperations(self, s: str) -> int:
        alt1 = [abs(k%2-int(s[k])) for k in range(len(s))]
        alt2 = [abs(abs(k%2-1)-int(s[k])) for k in range(len(s))]
        return min(sum(alt1), sum(alt2))
    