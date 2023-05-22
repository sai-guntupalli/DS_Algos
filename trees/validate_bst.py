# https://leetcode.com/problems/validate-binary-search-tree/editorial/

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Input: root = [2,1,3]
# Output: true

from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import math


class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(root, left, right):
            # empty tree is valid BST
            if not root:
                return True

            if root.val <= left or root.val >= right:
                return False

            return (validate(root.left, left, root.val)
                    and validate(root.right, root.val, right))

        res = validate(root, -math.inf, math.inf)
        return res


if __name__ == '__main__':
    from utils import *

    input = [5, 3, None, 2, 4, None, None, 1, None, None, None, None, None]
    # input = [2, 1, 3]
    tree = deserialize(input)

    res = Solution().isValidBST(tree)

    print(res)
