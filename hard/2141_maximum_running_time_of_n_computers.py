# https://leetcode.com/problems/maximum-running-time-of-n-computers
# hard
# daily mock interview
class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        batteries.sort()
        comps = batteries[-n:]
        reserve = sum(batteries[:-n])

        for i in range(1, len(comps)):
            needed = (comps[i] - comps[i - 1]) * i
            if reserve <= needed:
                return comps[i - 1] + reserve // i
            reserve -= needed

        return comps[-1] + reserve // n

