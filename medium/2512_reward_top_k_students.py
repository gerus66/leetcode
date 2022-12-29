# https://leetcode.com/problems/reward-top-k-students
# medium
# biweekly contest 94 - virtual
import bisect
from typing import List


class Solution:
    @staticmethod
    def count_word(words, pos, neg):
        count = 0
        for w in words:
            if w in pos:
                count += 3
            elif w in neg:
                count -= 1
        return count

    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        pos = set(positive_feedback)
        neg = set(negative_feedback)
        rank = []
        for st_id, rep in zip(student_id, report):
            st_rank = self.count_word(rep.split(' '), pos, neg)
            bisect.insort(rank, (-st_rank, st_id))
        return [r[1] for r in rank[:k]]
