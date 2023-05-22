from drawtree import draw_level_order
from typing import Optional
from utils import *

# problem stmt : https://leetcode.com/problems/range-sum-of-bst/description/

# Given the root node of a binary search tree and two integers low and high,
#   return the sum of values of all nodes with a value in the inclusive range [low, high].

# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

# draw_level_order('[10,5,15,3,7,13,18,1,#,6]')


# tree definition
class TreeNode(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rangeSumBST(self, root: Optional[TreeNode], low: int,
                    high: int) -> int:

        sum = 0

        def find_sum(node, low, high):
            nonlocal sum
            if not node:
                return 0

            if low <= node.val <= high:
                sum += node.val

            if root.val >= low:
                find_sum(node.left, low, high)

            if root.val <= high:
                find_sum(node.right, low, high)

        find_sum(root, low, high)

        return sum


if __name__ == '__main__':
    input = [10, 5, 15, 3, 7, None, 18]
    low = 7
    high = 15
    root = deserialize(input)
    res = Solution().rangeSumBST(root, low, high)

    print(f"sum of nodes in the range {low} and {high} is : {res}")
