# https://leetcode.com/problems/add-binary
# easy
# daily
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        big, small = (a, b) if len(a) > len(b) else (b, a)
        small = "0" * (len(big) - len(small)) + small
        prev, res = 0, ""
        for aa, bb in zip(reversed(small), reversed(big)):
            cur = prev + int(aa) + int(bb)
            prev, cur = divmod(cur, 2)
            res += str(cur)
        if prev:
            res += str(prev)
        return ''.join(reversed(res))
    