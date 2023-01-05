# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons
# medium
# daily
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sort_points = sorted(points, key=lambda x: x[1])
        arrows, last_arrow = 1, sort_points[0][1]
        for balloon in sort_points[1:]:
            if balloon[0] <= last_arrow:
                continue
            arrows, last_arrow = arrows + 1, balloon[1]
        return arrows
