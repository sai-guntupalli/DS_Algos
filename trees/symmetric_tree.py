# https://leetcode.com/problems/symmetric-tree/description/
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# Input: root = [1,2,2,3,4,4,3]
# Output: true

from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def validate(left, right):

            if not left and not right:
                return True

            if not left or not right:
                return False

            if left.val != right.val:
                return False

            return validate(left.left, right.right) and validate(
                left.right, right.left)

        res = validate(root.left, root.right)

        return res


if __name__ == '__main__':
    from utils import *

    tree = [1, 2, 2, 3, 4, 4, 3]
    tree = deserialize(tree)

    res = Solution().isSymmetric(tree)

    print(res)
