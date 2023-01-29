# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label
# medium
# practice - missed daily
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [1 for _ in range(n)]
        tree = {i: [[], {ch: 1}] for i, ch in enumerate(labels)}
        for [fr, to] in edges:
            tree[fr][0].append(to)
            tree[to][0].append(fr)

        to_go, seen, handled = [0], set(), set()
        while to_go:
            index = to_go[-1]
            if index not in seen:
                seen.add(index)
                for child in tree[index][0]:
                    if child not in seen:
                        to_go.append(child)
            else:
                to_go.pop()
                for child in tree[index][0]:
                    if child in handled:
                        for k, v in tree[child][1].items():
                            tree[index][1][k] = tree[index][1].get(k, 0) + v
                ans[index] = tree[index][1][labels[index]]
                handled.add(index)
        return ans
