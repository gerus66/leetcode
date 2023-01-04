# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks
# medium
# daily
from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = Counter(tasks)
        count = 0
        for v in d.values():
            if v == 1:
                return -1
            count += v // 3 + (1 if v % 3 else 0)
        return count
    