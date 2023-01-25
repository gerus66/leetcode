# https://leetcode.com/problems/snakes-and-ladders
# medium
# practice - missed daily
from typing import List


class Solution:
    @staticmethod
    def plain_board(board):
        plain_board = []
        for i, row in enumerate(board[::-1]):
            if i % 2:
                plain_board.extend(row[::-1])
            else:
                plain_board.extend(row)
        return plain_board

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        b = [[x, -1] for x in self.plain_board(board)]
        b[0][1] = 0
        len_b = len(b)
        i = 0
        while i < len_b:
            i += 1
            steps = b[i-1][1]
            if steps == -1:
                continue  # cell is unachievable
            for j in range(i, min(i+6, len_b)):
                [port, j_steps] = b[j]
                if port == -1:  # no teleport at j cell
                    b[j][1] = steps+1 if j_steps == -1 else min(j_steps, steps+1)
                elif port >= i:  # stairs teleport at j cell
                    b[port-1][1] = steps + 1 if b[port-1][1] == -1 else min(b[port-1][1], steps + 1)
                elif b[port-1][1] == -1 or b[port-1][1] > steps+1:  # snake teleport at j cell
                    b[port - 1][1] = steps + 1
                    i = port - 1
        return b[-1][1]
