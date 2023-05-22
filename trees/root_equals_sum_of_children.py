from utils import *
from typing import Optional

# https://leetcode.com/problems/root-equals-sum-of-children/

# You are given the root of a binary tree that consists of exactly 3
# nodes: the root, its left child, and its right child.

# Return true if the value of the root is equal to the sum of the values
#  of its two children, or false otherwise.


class Solution:

    def checkTree(self, root: Optional[TreeNode]) -> bool:
        sum = -root.val

        def find_sum1(root):
            nonlocal sum
            if root:
                sum += root.val
                find_sum1(root.left)
                find_sum1(root.right)

        find_sum1(root)
        return sum == root.val


if __name__ == '__main__':
    input = [10, 4, 6]
    root = deserialize(input)
    res = Solution().checkTree(root)

    print(f"res is : {res}")