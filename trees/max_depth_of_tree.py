# https://leetcode.com/problems/maximum-depth-of-binary-tree/solutions/?orderBy=most_votes

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Input: root = [3,9,20,null,null,15,7]
# Output: 3

from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def maxLen(root, depth):
            if not root:
                return depth

            return max(maxLen(root.left, depth + 1),
                       maxLen(root.right, depth + 1))

        return maxLen(root, 0)


if __name__ == '__main__':
    from utils import *

    # tree = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
    tree = [2, None, 3, None, 4, None, 5, None, 6]
    tree = deserialize(tree)

    res = Solution().maxDepth(tree)

    print(res)
