# https://leetcode.com/problems/evaluate-division
# medium
# daily mock interview
class Solution:
    @staticmethod
    def dfs(graph: dict, start: str, end: str) -> float:
        stack, seen = [(start, 1.0)], {start}
        while stack:
            cur_node, cur_val = stack.pop()
            if cur_node not in graph:
                return -1.0
            if cur_node == end:
                return cur_val
            for next_node, mult in graph[cur_node]:
                if next_node not in seen:
                    seen.add(next_node)
                    stack.append((next_node, cur_val * mult))
        return -1.0

    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = dict()
        for (up, down), val in zip(equations, values):
            graph.setdefault(up, []).append((down, 1 / val))
            graph.setdefault(down, []).append((up, val))

        return [self.dfs(graph, down, up) for up, down in queries]
