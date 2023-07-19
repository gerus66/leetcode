# https://leetcode.com/problems/relative-ranks
# easy
# speed practice of easy tasks
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort_scores = sorted([(s, i) for i, s in enumerate(score)], reverse=True)
        ranks = sorted([(i, k) for k, (_, i) in enumerate(sort_scores)])
        template = ["Gold Medal","Silver Medal","Bronze Medal"]
        return [str(k+1) if k > 2 else template[k] for _, k in ranks]
