from utils import *
from typing import Optional

# https://leetcode.com/problems/merge-two-binary-trees/description/

# You are given two binary trees root1 and root2.

# Imagine that when you put one of them to cover the other, some nodes of the
# two trees are overlapped while the others are not.
# You need to merge the two trees into a new binary tree.
# The merge rule is that if two nodes overlap, then sum node values up as the
# new value of the merged node. Otherwise, the NOT null node will be used as
# the node of the new tree.

# Return the merged tree.

# Note: The merging process must start from the root nodes of both trees.


class Solution:

    def mergeTrees(self, t1: Optional[TreeNode],
                   t2: Optional[TreeNode]) -> Optional[TreeNode]:

        res_list = []

        def merge(t1, t2):

            if t1 and t2:
                res_list.append(t1.val + t2.val)
                t1.val += t2.val

                t1.left = merge(t1.left, t2.left)
                t1.right = merge(t1.right, t2.right)
                return t1

            else:
                if t1:
                    res_list.append(t1.val)
                if t2:
                    res_list.append(t2.val)
                return t1 or t2

        merge(t1, t2)
        return res_list


if __name__ == '__main__':
    ip1 = [1, 3, 2, 5]
    ip2 = [2, 1, 3, None, 4, None, 7]
    root1 = deserialize(ip1)
    root2 = deserialize(ip2)
    res = Solution().mergeTrees(root1, root2)
    res = deserialize(res)
    print(f"lonley nodes : {res}")
