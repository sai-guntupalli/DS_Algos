# https://leetcode.com/problems/binary-tree-right-side-view/description/
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the
# res you can see ordered from top to bottom.

# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

from typing import Optional, List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        level = 0

        def find_right_res(root, level):
            if not root:
                return

            if len(res) <= level:
                res.append(root.val)

            #change order to change the view angle. right first for right view,
            # left first for left view.
            find_right_res(root.right, level + 1)
            find_right_res(root.left, level + 1)

        find_right_res(root, level)

        return res


if __name__ == '__main__':
    from utils import *

    input = [5, 3, None, 2, 4, None, None, 1, None, None, None, None, None]
    tree = deserialize(input)

    res = Solution().rightSideView(tree)

    print(res)
