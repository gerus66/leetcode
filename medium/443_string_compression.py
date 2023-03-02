# https://leetcode.com/problems/string-compression
# medium
# daily
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        prev_ch, count, j = chars[0], 1, 0
        for ch in chars[1:]+[chr(ord(chars[-1]) + 1)]:
            if ch == prev_ch:
                count += 1
                continue
            chars[j], prev_ch, j = prev_ch, ch, j + 1
            if count > 1:
                c = str(count)
                chars[j:j+len(c)] = c
                j, count = j + len(c), 1
        return j
