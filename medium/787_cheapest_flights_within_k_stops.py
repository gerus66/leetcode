# https://leetcode.com/problems/cheapest-flights-within-k-stops
# medium
# practice - missed daily
from typing import List
from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = defaultdict(list)
        for fl in flights:
            d[fl[0]].append((fl[2], fl[1]))
        h = []
        for fl in d.get(src, []):
            heapq.heappush(h, (fl[0], 0, fl[1]))
        been_here = {src: 0}

        while h:
            try_to_fly = heapq.heappop(h)
            if try_to_fly[2] == dst:
                return try_to_fly[0]
            if try_to_fly[1] == k:
                continue  # one more flight will overflow k
            if try_to_fly[2] in been_here and been_here[try_to_fly[2]] <= try_to_fly[1]:
                continue  # been here with less price and less/equal stops value
            been_here[try_to_fly[2]] = try_to_fly[1]
            for fl in d.get(try_to_fly[2], []):
                heapq.heappush(h, (try_to_fly[0] + fl[0], try_to_fly[1] + 1, fl[1]))
        return -1
