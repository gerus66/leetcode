# https://leetcode.com/problems/daily-temperatures
# medium
# training - missed daily
from typing import List
import bisect


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0]
        hillside = [(temperatures[-1], 1)]
        for t in temperatures[-2::-1]:
            if t < hillside[-1][0]:
                hillside.append((t, 1))
                results.append(1)
                continue
            p = bisect.bisect_right(hillside[::-1], t, key=lambda x: x[0])
            if p >= len(hillside):
                results.append(0)
                hillside = [(t, 1)]
            else:
                days = sum(h[1] for h in hillside[len(hillside)-p:]) + 1
                results.append(days)
                hillside = hillside[:len(hillside)-p]
                hillside.append((t, days))

        return results[::-1]
    