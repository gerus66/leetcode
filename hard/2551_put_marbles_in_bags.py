# https://leetcode.com/problems/put-marbles-in-bags
# hard
# daily
from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        borders = [weights[i]+weights[i+1] for i in range(len(weights)-1)]
        borders.sort()
        return sum(borders[-(k-1):]) - sum(borders[:(k-1)])
    