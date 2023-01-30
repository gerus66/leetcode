# https://leetcode.com/problems/longest-path-with-different-adjacent-characters
# hard
# practice - missed daily
from typing import List


class Solution:
    @staticmethod
    def tree_height(start, forest, to_remember):
        to_go, seen, cur_len = [start], set(), 0
        max_len, index = 0, start
        while to_go:
            node = to_go.pop()
            if node in seen:
                cur_len -= 1
            else:
                seen.add(node)
                to_remember.discard(node)
                cur_len += 1
                if cur_len > max_len:
                    max_len, index = cur_len, node
                for ch in forest.get(node, []):
                    if ch not in seen:
                        to_go.extend([node, ch])
        return max_len, index

    def tree_max_len(self, start, forest, to_remember):
        _, begin = self.tree_height(start, forest, to_remember)
        max_len, _ = self.tree_height(begin, forest, to_remember)
        return max_len

    def longestPath(self, parent: List[int], s: str) -> int:
        to_remember = {0}
        forest = {}
        for fr, to in enumerate(parent[1:], start=1):
            if s[fr] == s[to]:
                to_remember.update({fr, to})
            else:
                forest[fr] = forest.get(fr, []) + [to]
                forest[to] = forest.get(to, []) + [fr]
        max_len = 0
        while to_remember:
            node = to_remember.pop()
            max_len = max(max_len, self.tree_max_len(node, forest, to_remember))
        return max_len
