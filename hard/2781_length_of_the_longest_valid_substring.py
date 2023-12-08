# https://leetcode.com/problems/length-of-the-longest-valid-substring
# hard
# daily mock interview
class Solution:
    @staticmethod
    def shortest_forbidden(s: str, prefixes: set, sub_prefixes: set) -> int:
        for i in range(1, len(s) + 1):
            cur_sub = s[(len(s) - i):]
            if cur_sub in prefixes:
                return i
            if cur_sub not in sub_prefixes:
                return 0
        return 0

    def longestValidSubstring(self, word: str, forbidden: list[str]) -> int:
        prefixes, sub_prefixes = set(forbidden), set()
        for prefix in forbidden:
            for i in range(1, len(prefix)):
                if prefix[i:] not in prefixes:
                    sub_prefixes.add(prefix[i:])

        max_len, cur_len = 0, 0
        for i in range(1, len(word) + 1):
            if (fob_len := self.shortest_forbidden(word[:i], prefixes, sub_prefixes)):
                max_len, cur_len = max(max_len, cur_len), min(cur_len + 1, fob_len - 1)
            else:
                cur_len += 1

        return max(cur_len, max_len)
