# https://leetcode.com/problems/find-the-town-judge
# easy
# daily
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #judges = {range(1, n+1)} - {t[0] for t in trust}  # judge believe nobody
        trust_no_one = {j: 0 for j in set(range(1, n+1)) - {t[0] for t in trust}}
        for t in trust:
            if t[1] in trust_no_one:
                trust_no_one[t[1]] += 1
        maybe_judges = [k for k, v in trust_no_one.items() if v == n-1]
        return maybe_judges[0] if len(maybe_judges) == 1 else -1
