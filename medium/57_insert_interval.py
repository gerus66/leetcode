# https://leetcode.com/problems/insert-interval
# medium
# practice - missed daily
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals or intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals

        res, i, n = [], 0, len(intervals)
        while intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        res.append([min(newInterval[0], intervals[i][0])])
        while i < n and intervals[i][1] < newInterval[1]:
            i += 1
        if i == n:
            res[-1].append(max(intervals[i-1][1], newInterval[1]))
            return res
        if newInterval[1] < intervals[i][0]:
            res[-1].append(newInterval[1])
        else:
            res[-1].append(intervals[i][1])
            i += 1
        res += intervals[i:]
        return res
