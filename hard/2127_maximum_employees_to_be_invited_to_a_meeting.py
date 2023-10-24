# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting
# hard
# Uber list
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.d = defaultdict(set)

    def find_pairs(self):  # O(N)
        pairs = set()
        for k, v in self.d.items():
            for el in list(v):
                if el in self.d and k in self.d[el]:
                    pairs.add(tuple(sorted([k, el])))
        return pairs

    def max_depth(self, root, other):  # O(N)
        cur_dep, max_dep = 1, 1
        seen = {root}
        to_go = [(ch, cur_dep+1) for ch in self.d[root] if ch != other]
        while to_go:
            cur, cur_dep = to_go.pop()
            seen.add(cur)
            chs = [(ch, cur_dep+1) for ch in self.d.get(cur, []) if ch not in seen]
            if chs:
                to_go.extend(chs)
            else:
                max_dep = max(max_dep, cur_dep)
        return max_dep

    def max_cycle(self):  # O(N)
        max_len = 1
        while self.d:
            cur_len = 1
            k, v = self.d.popitem()
            seen = {k}
            to_go = [(ch, cur_len + 1) for ch in v]
            while to_go:
                cur, cur_len = to_go.pop()
                seen.add(cur)
                for ch in self.d.pop(cur, []):
                    if ch in seen:
                        max_len = max(max_len, cur_len)
                    else:
                        to_go.append((ch, cur_len+1))
        return max_len

    def maximumInvitations(self, favorite: List[int]) -> int:
        for i, f in enumerate(favorite):
            self.d[f].add(i)

        pairs = self.find_pairs()
        all_pairs_score = 0
        for p in pairs:
            all_pairs_score += self.max_depth(p[0], p[1]) + self.max_depth(p[1], p[0])
        max_cycle = self.max_cycle()
        return max(all_pairs_score, max_cycle)


names = ['favorite']

tests = [
    [[2,2,1,2]],
    [[1,2,0]],
    [[3,0,1,4,1]],
    [[1,0,0,2,1,4,7,8,9,6,7,10,8]],
    [[1,0,3,2,5,6,7,4,9,8,11,10,11,12,10]],
]

answers = [
    3,
    3,
    4,
    6,
    11,
]

for ii, (t, a) in enumerate(zip(tests, answers)):
    sol = Solution().maximumInvitations(**{n: v for n, v in zip(names, t)})
    try:
        assert sol == a
    except AssertionError:
        print(f'\033[91mtest {ii} fail: {sol} != {a}\n\033[0m')
    else:
        print(f'\033[32mtest {ii} OK\n\033[0m')


