# https://leetcode.com/problems/max-points-on-a-line
# hard
# daily
from typing import List
import math


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        lines = {}
        for i, p in enumerate(points):
            for j, pair_p in enumerate(points):
                if j == i:
                    continue
                k = p[1] - pair_p[1]
                denominator = p[0] - pair_p[0]
                k_gcd = math.gcd(k, denominator)
                k /= k_gcd
                denominator /= k_gcd
                b = denominator * pair_p[1] - k * pair_p[0]
                if lines.get((k, b, denominator)) is None:
                    lines[(k, b, denominator)] = {(p[0], p[1]), (pair_p[0], pair_p[1])}
                else:
                    lines[(k, b, denominator)].add((p[0], p[1]))
                    lines[(k, b, denominator)].add((pair_p[0], pair_p[1]))
        return max(len(v) for v in lines.values()) if lines else 1
