# https://leetcode.com/problems/count-of-matches-in-tournament
# easy
# speed practice of easy tasks
class Solution:
    def numberOfMatches(self, n: int) -> int:
        count, teams = 0, n
        while teams > 1:
            count += teams // 2
            teams = teams // 2 + teams % 2
        return count
