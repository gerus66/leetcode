# https://leetcode.com/problems/remove-stones-to-minimize-the-total
# medium
# daily
from typing import List
import heapq


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        q = [-p for p in piles]
        heapq.heapify(q)
        for i in range(k):
            elem = heapq.heappop(q)
            heapq.heappush(q, elem//2)
        return -sum(q)
    