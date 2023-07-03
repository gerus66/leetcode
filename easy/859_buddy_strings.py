# https://leetcode.com/problems/buddy-strings
# easy
# daily
from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return any(v > 1 for v in Counter(s).values())
        diff, founded = None, False
        for ss, gg in zip(s, goal):
            if ss != gg:
                if founded == True:
                    return False
                if diff is None:
                    diff = (ss, gg)
                elif diff == (gg, ss):
                    founded = True
                else:
                    return False
        return founded

