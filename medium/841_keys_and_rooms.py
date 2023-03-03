# https://leetcode.com/problems/keys-and-rooms
# medium
# practice - missed daily
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        to_go, seen = rooms[0], set([0])
        while to_go:
            if (room := to_go.pop()) in seen:
                continue
            seen.add(room)
            to_go += rooms[room]
        return set(range(len(rooms))) == seen
