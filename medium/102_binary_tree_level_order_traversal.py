# https://leetcode.com/problems/binary-tree-level-order-traversal
# medium
# Uber interview prep
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(N) - time
# O(N) - space


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        output = []
        stack, next_stack = [root] if root else [], []
        while stack:
            level = []
            for node in stack:
                level.append(node.val)
                for child in (node.left, node.right):
                    if child is not None:
                        next_stack.append(child)
            output.append(level)
            stack, next_stack = next_stack, []
        return output

