# https://leetcode.com/problems/increasing-order-search-tree/description/
# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree,
# and every node has no left child and only one right child.


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)

        inorder(root)

        root = TreeNode(nodes[0])
        temp = root

        for node in nodes[1:]:
            temp.right = TreeNode(node)
            temp = temp.right

        # return root
        return nodes


if __name__ == '__main__':
    from utils import *

    input = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
    tree = deserialize(input)

    res = Solution().increasingBST(tree)

    print(res)

    deserialize(res)
