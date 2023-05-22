# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
#  (i.e., from left to right, then right to left for the next level and alternate between).

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

from typing import Optional, List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        level = 0

        def traversal(root, level):
            if not root:
                return

            if len(res) < level + 1:
                res.append([])

            if level % 2 == 0:
                res[level].append(root.val)
            else:
                # for levels, 1,3,5 etc, reverse the level elements
                res[level].insert(0, root.val)

            traversal(root.left, level + 1)
            traversal(root.right, level + 1)

        traversal(root, level)
        return res


if __name__ == '__main__':
    from utils import *
    ip = [1, 2, 3, 4, 5, 6, 7]
    root = deserialize(ip)
    res = Solution().zigzagLevelOrder(root)
    # res2 = Solution().levelOrderRecursive(root2)

    print(f"level order zigzag recursive : {res}")
    # print(f"level order recursive : {res2}")