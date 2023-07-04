# https://leetcode.com/problems/single-number-ii
# medium
# daily
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        state = [0 for _ in range(33)]  # reversed, first bit is for sign
        for el in nums:
            last_bit = 1 if el < 0 else 0
            el_bin = [last_bit] + [int(x) for x in bin(abs(el))[-1:1:-1]]
            state[:len(el_bin)] = [x+y if x+y < 3 else 0 for x, y in zip(state, el_bin)]
            # print(state)
        return sum(2**i for i, x in enumerate(state[1:]) if x == 1) * (-1 if state[0] else 1)
