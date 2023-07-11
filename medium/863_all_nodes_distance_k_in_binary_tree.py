# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree
# medium
# daily
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        q = deque([root])
        tree = {root.val: []}
        while q:
            cur = q.pop()
            if cur is None:
                continue
            for child in [cur.left, cur.right]:
                if child is not None:
                    tree[cur.val].append(child.val)
                    tree[child.val] = [cur.val]
            q.extendleft([cur.left, cur.right])

        q = deque([(target.val, 0)])
        seen = set()
        res = []
        while q:
            cur, dist = q.pop()
            if dist > k:
                return res
            if dist == k:
                res.append(cur)
                continue
            for child in tree[cur]:
                if child not in seen:
                    q.appendleft((child, dist + 1))
            seen.add(cur)
        return res
