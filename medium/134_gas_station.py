# https://leetcode.com/problems/gas-station
# medium
# practice - missed daily
from collections import deque
from typing import List


class Solution:
    @staticmethod
    def zip_diff(diff):
        while diff[0][0] < 0:
            deque.rotate(diff, -1)
        while diff[-1][0] > 0:
            deque.rotate(diff, 1)
        i, zipped = 0, deque([[0, diff[0][1]]])
        while i < len(diff):
            if zipped[-1][0] >= 0 and zipped[-1][0] + diff[i][0] >= 0:
                zipped[-1][0] += diff[i][0]
            else:
                zipped.append(diff[i])
            i += 1
        return zipped

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = deque([g-c, i] for i, (g, c) in enumerate(zip(gas, cost)))
        if len(diff) == 1:
            return 0 if diff[0][0] >= 0 else -1
        zipped = self.zip_diff(diff)
        while 1 < len(zipped) < len(diff):
            diff = zipped
            zipped = self.zip_diff(diff)
        return zipped[0][1] if len(zipped) == 1 else -1
