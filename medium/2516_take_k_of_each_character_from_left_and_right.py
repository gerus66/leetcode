# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right
# medium
# training after contest - weekly 325 - virtual
import math
from collections import deque


class Solution:
    def __init__(self):
        self.minimum = math.inf
        self.d = {}

    def clean_from_left(self, to_delete, stack):
        deleted = 0
        while stack and self.d[stack[0]] and deleted < to_delete:
            self.d[stack[0]] -= 1
            stack.popleft()
            deleted += 1
        self.minimum = min(self.minimum, len(stack))
        return deleted

    def takeCharacters(self, s: str, k: int) -> int:
        self.d = {ch: -k for ch in "abc"}
        for ch in s:
            self.d[ch] += 1
        if min(v for v in self.d.values()) < 0:
            return -1

        stack_1 = deque(s)
        stack_2 = deque(s[::-1])
        self.minimum = len(s)
        to_delete = len(s) - self.clean_from_left(len(s), stack_2)
        while stack_1 and to_delete:
            stack_2.append(stack_1.pop())
            self.d[stack_2[-1]] += 1
            to_delete -= self.clean_from_left(to_delete, stack_2)
        return self.minimum
