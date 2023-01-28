# https://leetcode.com/problems/data-stream-as-disjoint-intervals
# hard
# daily
import bisect
from typing import List


class SummaryRanges:
    # (value, 0: is_st / 1: is_fin)
    def __init__(self):
        self.stream = list()
        self.n = 0

    def _is_st(self, i):
        return not self.stream[i][1]

    def _is_fin(self, i):
        return self.stream[i][1]

    def addNum(self, value: int) -> None:
        i = bisect.bisect(self.stream, (value, -1))
        # value already in the stream
        if i < self.n and (self._is_fin(i) or self.stream[i][0] == value):
            return

        # just replace existing border
        new_st, new_fin = False, False
        if i > 0 and self.stream[i-1][0] == value-1 and self._is_fin(i-1):
            self.stream[i-1], new_fin = (value, 1), True
        if i < self.n and self.stream[i][0] == value+1 and self._is_st(i):
            self.stream[i], new_st = (value, 0), True
        if new_st != new_fin:
            return

        # merge and delete inner borders
        if new_st and new_fin:
            del self.stream[i-1:i+1]
            self.n -= 2
            return

        # insert new interval
        self.stream[i:i] = [(value, 0),(value,1)]
        self.n += 2

    def getIntervals(self) -> List[List[int]]:
        intervals = []
        for (num, is_fin) in self.stream:
            if not is_fin:
                intervals.append([num])
            else:
                intervals[-1].append(num)
        return intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
