# https://leetcode.com/problems/reorder-list
# medium
# Uber interview prep

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def get_length(head: ListNode | None) -> int:
        length, node = 0, head
        while node:
            length, node = length + 1, node.next
        return length

    @staticmethod
    def reverse(head: ListNode | None) -> ListNode | None:
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
        return prev

    @staticmethod
    def merge(head1: ListNode | None, head2: ListNode | None) -> None:
        tail, cur1, cur2 = head1, head1.next if head1 else None, head2
        while cur1 and cur2:
            tail.next = cur2
            tail, cur2 = tail.next, cur2.next
            tail.next = cur1
            tail, cur1 = tail.next, cur1.next
        if cur1:
            tail.next = cur1
        if cur2:
            tail.next = cur2

    def reorderList(self, head: ListNode | None) -> None:
        length = self.get_length(head)
        i, prev_node, cur_node = 0, None, head
        while i <= (length // 2):
            i, prev_node, cur_node = i + 1, cur_node, cur_node.next
        if prev_node:
            prev_node.next = None

        reversed_head = self.reverse(cur_node)

        self.merge(head, reversed_head)
