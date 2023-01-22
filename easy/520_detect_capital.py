# https://leetcode.com/problems/detect-capital
# easy
# practice - missed daily
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        if word[0].islower() and word[1].isupper():
            return False
        wait_capital = word[0].isupper() and word[1].isupper()
        return all(ch.isupper() == wait_capital for ch in word[2:])
    