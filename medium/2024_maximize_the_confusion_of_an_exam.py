# https://leetcode.com/problems/maximize-the-confusion-of-an-exam
# medium
# daily
class Solution:
    def window(self, fr):
        max_len, cur_len = 0, 0
        i_left, i_right, turned = 0, 0, 0
        while i_right < len(self.str):
            while turned <= self.k and i_right < len(self.str):
                i_right, cur_len = i_right + 1, cur_len + 1
                if self.str[i_right-1] == fr:
                    turned += 1
            max_len = max(max_len, cur_len-1)
            while turned > self.k and i_left <= i_right:
                if self.str[i_left] == fr:
                    turned -= 1
                i_left, cur_len = i_left + 1, cur_len - 1
            max_len = max(max_len, cur_len)
        return max_len

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        self.str = answerKey
        self.k = k
        return max(self.window('T'), self.window('F'))
