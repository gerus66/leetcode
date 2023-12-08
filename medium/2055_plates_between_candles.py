# https://leetcode.com/problems/plates-between-candles
# medium
# daily mock interview
class Solution:
    @staticmethod
    def count_plates(s: str, storage: list, query: list) -> int:
        left, right = query
        left_count = storage[left] if s[left] == '|' else storage[storage[left][1]]
        right_count = storage[right] if s[right] == '|' else storage[storage[right][0]]
        return max(0, right_count - left_count)

    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        storage = []
        cur_plates, all_plates = 0, 0
        last_candle_idx = -1
        for i, ch in enumerate(s):
            if ch == '*':
                cur_plates += 1
                storage.append([last_candle_idx, last_candle_idx])
            if ch == '|':
                all_plates += cur_plates
                cur_plates = 0
                storage.append(all_plates)
                for j in range(last_candle_idx + 1, i):
                    storage[j][1] = i
                last_candle_idx = i
        storage.append(0)

        return [self.count_plates(s, storage, query) for query in queries]



