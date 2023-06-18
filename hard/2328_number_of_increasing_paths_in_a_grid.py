# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid
# hard
# daily
from collections import defaultdict
import itertools
from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        d = defaultdict(list)
        ans = len(grid) * len(grid[0])
        for i, row in enumerate(grid):
            for j, el in enumerate(row):
                if i > 0:
                    if grid[i-1][j] < el:
                        d[(i-1,j)].append((i,j))
                    elif grid[i-1][j] > el:
                        d[(i,j)].append((i-1,j))
                if j > 0:
                    if grid[i][j-1] < el:
                        d[(i,j-1)].append((i,j))
                    elif grid[i][j-1] > el:
                        d[(i,j)].append((i,j-1))
        branches = d.keys() - set(itertools.chain.from_iterable(d.values()))
        seen = defaultdict(int)
        while branches:
            k = branches.pop()
            # coordinates, depth, backtracking
            to_go = [(k, 0, False)]
            while to_go:
                (i, j), depth, caching = to_go.pop()
                if caching:
                    seen[(i,j)] += count
                    count = seen[(i,j)] + 1
                elif (i, j) in seen:  # been here, know score, just rise ans
                    ans += depth * (seen[(i,j)] + 1)
                    count = seen[(i,j)] + 1
                else:
                    ans += depth
                    if (i, j) in d:  # go further to depth
                        for x in d[(i,j)]:
                            to_go.extend([((i,j), depth, True), (x, depth+1, False)])
                    else:  # end of local branch
                        count = 1
        return ans % (10**9 + 7)
