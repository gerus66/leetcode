# https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream
# medium
# biweekly contest 95
class DataStream:

    def __init__(self, value: int, k: int):
        self.sample = value
        self.need_count = k
        self.current_count = 0

    def consec(self, num: int) -> bool:
        if num == self.sample:
            self.current_count += 1
        else:
            self.current_count = 0
        return self.current_count >= self.need_count

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
