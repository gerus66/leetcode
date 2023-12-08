# https://leetcode.com/problems/time-based-key-value-store
# medium
# practice class design
class TimeMap:

    def __init__(self):
        self.vault: dict[str, list[tuple[int]]] = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vault.setdefault(key, [(-1, "")]).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.vault.get(key, [(-1, "")])
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp and (mid == len(arr) - 1 or timestamp < arr[mid + 1][0]):
                return arr[mid][1]
            if arr[mid][0] < timestamp:
                left = mid
            else:
                right = mid

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)