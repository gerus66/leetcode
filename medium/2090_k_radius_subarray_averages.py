# https://leetcode.com/problems/k-radius-subarray-averages
# medium
# daily
from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        avg = [-1 for _ in range(min(k, length))]
        cur_sum = sum(nums[:min(2*k, length)])
        i = k
        while i < length - k:
            cur_sum += nums[i+k]
            if i > k:
                cur_sum -= nums[i-k-1]
            avg.append(cur_sum // (2*k+1))
            i += 1
        while i < length:
            avg.append(-1)
            i += 1
        return avg
