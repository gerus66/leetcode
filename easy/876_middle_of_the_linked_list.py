# https://leetcode.com/problems/middle-of-the-linked-list
# easy
# training - missed daily
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        it, itx2 = head, head
        while itx2 is not None and itx2.next is not None:
            it = it.next
            itx2 = itx2.next.next
        return it
