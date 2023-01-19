# https://leetcode.com/problems/subarray-sums-divisible-by-k
# medium
# daily
from typing import List
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_d = defaultdict(int)
        count, cur_sum = 0, 0
        for num in nums:
            cur_sum += num
            rem = cur_sum % k
            if not rem:
                count += 1
            count += rem_d[rem]
            rem_d[rem] += 1
        return count
