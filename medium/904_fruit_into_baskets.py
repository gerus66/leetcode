# https://leetcode.com/problems/fruit-into-baskets
# medium
# daily
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket, max_fruits, cur_fruits, left = dict(), 0, 0, 0
        for f in fruits:
            if f in basket:
                basket[f] += 1
                cur_fruits += 1
            elif len(basket) < 2:
                basket[f] = 1
                cur_fruits += 1
            else:
                max_fruits = max(max_fruits, cur_fruits)
                while len(basket) > 1:
                    basket[fruits[left]] -= 1
                    cur_fruits -= 1
                    if not basket[fruits[left]]:
                        basket.pop(fruits[left])
                    left += 1
                basket[f] = 1
                cur_fruits += 1
        return max(max_fruits, cur_fruits)
