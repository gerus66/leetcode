# https://leetcode.com/problems/categorize-box-according-to-criteria
# easy
# biweekly contest 95
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        heavy = mass >= 100
        for d in (length, width, height):
            if d >= 10**4:
                return "Both" if heavy else "Bulky"
        if length * width * height >= 10**9:
            return "Both" if heavy else "Bulky"
        return "Heavy" if heavy else "Neither"
