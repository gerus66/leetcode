# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree
# medium
# practice - missed daily
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = {i: [[], hasApple[i]] for i in range(n)}
        for [fr, to] in edges:
            tree[fr][0].append(to)
            tree[to][0].append(fr)
        to_go, seen, handled, count = [0], set(), set(), 0
        while to_go:
            index = to_go[-1]
            if index in seen:
                to_go.pop()
                if not tree[index][1]:
                    tree[index][1] = any(tree[x][1] for x in tree[index][0] if x in handled)
                count += 0 if not index else 1 if tree[index][1] else -1
                handled.add(index)
            else:
                seen.add(index)
                count += 1 if index else 0
                for child in tree[index][0]:
                    if child not in seen:
                        to_go.append(child)
        return count
