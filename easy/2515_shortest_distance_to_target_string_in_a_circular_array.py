# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array
# easy
# weekly 325 - virtual
from typing import List


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        count = 0
        left, right = startIndex, startIndex
        while count < n:
            if words[left] == target or words[right] == target:
                return count
            left, right = (left - 1) % n, (right + 1) % n
            count += 1
        return -1
