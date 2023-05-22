# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# Given the root of a binary tree, return the level order traversal of its nodes'
#  values. (i.e., from left to right, level by level).

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

from utils import *
from typing import Optional, List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def levelOrderIterative(root):
            if not root:
                return None

            res = []
            q = []

            q.append(root)

            while len(q) > 0:
                level = []

                for i in range(len(q)):
                    node = q.pop(0)

                    level.append(node.val)

                    if node.left != None:
                        q.append(node.left)

                    if node.right != None:
                        q.append(node.right)

                res.append(level)

            return res

        res = levelOrderIterative(root)
        return res

    def levelOrderRecursive(self, root):

        res = []
        level = 0

        def bfs(node, level):
            if not node:
                return None

            if len(res) < level + 1:
                res.append([])
            res[level].append(node.val)

            bfs(node.left, level + 1)
            bfs(node.right, level + 1)

        bfs(root, level)
        return res


if __name__ == '__main__':
    ip2 = [3, 9, 20, None, None, 15, 7]
    root2 = deserialize(ip2)
    res = Solution().levelOrder(root2)
    res2 = Solution().levelOrderRecursive(root2)

    print(f"level order iterative : {res}")
    print(f"level order recursive : {res2}")
