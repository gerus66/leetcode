# https://leetcode.com/problems/restore-ip-addresses
# medium
# practice - missed daily
from typing import List


class Solution:
    @staticmethod
    def is_valid_part(s):
        if not s:
            return False
        if len(s) > 1 and s[0] == '0':
            return False
        return int(s) < 256

    def find_part(self, s, count):
        if count == 4:  # last iteration
            return [s] if self.is_valid_part(s) else None
        res = []
        for i in range(1, 4):
            if self.is_valid_part(s[:i]):
                next_parts = self.find_part(s[i:], count + 1)
                if next_parts is not None:
                    for next_part in next_parts:
                        res.append(f'{s[:i]}.{next_part}')
        return res

    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.find_part(s, 1)
