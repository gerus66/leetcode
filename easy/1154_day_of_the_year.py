# https://leetcode.com/problems/day-of-the-year
# easy
# speed practice of easy tasks
class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        leap = not year%4 and (year%100 or not year%400)
        months = [31, (29 if leap else 28), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(months[:month-1]) + day
    