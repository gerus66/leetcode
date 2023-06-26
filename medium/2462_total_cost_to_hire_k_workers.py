# https://leetcode.com/problems/total-cost-to-hire-k-workers
# medium
# daily
import bisect
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        up, down = min(candidates, len(costs)//2), max(len(costs)-candidates, len(costs)//2)
        pull_up, pull_down = sorted(-x for x in costs[:up]), sorted(-x for x in costs[down:])
        total_cost = 0
        for _ in range(k):
            if pull_up and (not pull_down or pull_up[-1] >= pull_down[-1]):
                total_cost -= pull_up.pop()
                if up < down:
                    bisect.insort(pull_up, -costs[up])
                    up += 1
            else:
                total_cost -= pull_down.pop()
                if down > up:
                    down -= 1
                    bisect.insort(pull_down, -costs[down])
        return total_cost
