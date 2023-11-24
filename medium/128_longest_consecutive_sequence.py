# https://leetcode.com/problems/longest-consecutive-sequence
# medium
# Uber interview prep
class Solution:
    @staticmethod
    def merge(left_merge, right_merge, intervals):
        left, right = intervals[left_merge], intervals[right_merge]
        intervals[left], intervals[right] = right, left
        if left_merge != left:
            intervals.pop(left_merge, None)
        if right_merge != right:
            intervals.pop(right_merge, None)
        return left, right

    def longestConsecutive(self, nums: list[int]) -> int:
        max_len, seen, intervals = (1 if nums else 0), set(), dict()
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            intervals[num] = num
            left, right = num, num
            if num - 1 in intervals:
                left, right = self.merge(num - 1, num, intervals)
            if num + 1 in intervals:
                left, right = self.merge(num, num + 1, intervals)
            max_len = max(max_len, right - left + 1)
        return max_len
