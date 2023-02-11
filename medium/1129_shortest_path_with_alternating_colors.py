# https://leetcode.com/problems/shortest-path-with-alternating-colors
# medium
# daily
from typing import List


class Solution:
    @staticmethod
    def walk_tree(tree, blue, answer):
        to_go, next_to_go, seen, index, length = [0], [], [set(), set()], blue, 0
        while to_go:
            node = to_go.pop()
            if node not in seen[index]:
                seen[index].add(node)
                answer[node] = length if answer[node] == -1 else min(answer[node], length)
                next_to_go += [leaf for leaf in tree.get(node, [[], []])[index]]
            if not to_go:
                to_go, next_to_go, length = next_to_go, [], length + 1
                index = abs(index - 1)
        return answer

    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        d = dict()
        for [fr, to] in redEdges:
            d[fr] = [d.get(fr, [[], []])[0]+[to], d.get(fr, [[], []])[1]]
        for [fr, to] in blueEdges:
            d[fr] = [d.get(fr, [[], []])[0], d.get(fr, [[], []])[1]+[to]]
        answer = [-1 for _ in range(n)]
        answer = self.walk_tree(d, 0, answer)
        answer = self.walk_tree(d, 1, answer)
        return answer
