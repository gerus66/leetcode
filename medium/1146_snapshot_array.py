# https://leetcode.com/problems/snapshot-array
# medium
# daily
from dataclasses import dataclass
import bisect


@dataclass
class SnapEl:
    val: int = 0
    span: int = 0


class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[SnapEl()] for _ in range(length)]
        self.count_snaps = 0
        # print('init', self.arr)

    def set(self, index: int, val: int) -> None:
        self.arr[index].append(SnapEl(val, self.count_snaps))
        # print('set', self.arr)

    def snap(self) -> int:
        self.count_snaps += 1
        return self.count_snaps - 1

    def get(self, index: int, snap_id: int) -> int:
        all_snaps = self.arr[index]
        i = bisect.bisect_right(all_snaps, snap_id, key=lambda x: x.span)
        # print('get', self.arr)
        return all_snaps[i - 1].val

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
