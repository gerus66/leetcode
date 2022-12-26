# https://leetcode.com/problems/minimum-penalty-for-a-shop
# medium
# practice missed contest - biweekly 92
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        open_penalties = [0 if ch == 'Y' else 1 for ch in customers]
        prev_open = 0
        for i, ch in enumerate(customers):
            open_penalties[i] = prev_open
            prev_open = open_penalties[i] + (1 if ch == 'N' else 0)
        open_penalties.append(prev_open)

        close_penalties = [0 if ch == 'N' else 1 for ch in customers]
        prev_close = 0
        for i, ch in enumerate(customers[::-1]):
            close_penalties[i] = prev_close + (1 if ch == 'Y' else 0)
            prev_close = close_penalties[i]
        close_penalties = close_penalties[::-1]
        close_penalties.append(0)

        min_pen = len(customers)
        min_hour = 0
        for i, penalties in enumerate(zip(open_penalties, close_penalties)):
            penalties = penalties[0] + penalties[1]
            if penalties < min_pen:
                min_hour = i
                min_pen = penalties

        return min_hour
