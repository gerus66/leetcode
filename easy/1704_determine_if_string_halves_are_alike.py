# https://leetcode.com/problems/determine-if-string-halves-are-alike
# easy
# training - missed daily
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        alpha = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        count = 0
        for i in range(len(s)//2):
            count += 1 if s[i] in alpha else 0
            count -= 1 if s[-(i+1)] in alpha else 0
        return count == 0
