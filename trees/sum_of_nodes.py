from utils import *
from typing import Optional

# given a tree, find sum of its nodes


class Solution:

    def sumOfNodes(self, root: Optional[TreeNode]) -> bool:
        sum = 0

        def find_sum(root):
            nonlocal sum
            if root:
                sum += root.val
                find_sum(root.left)
                find_sum(root.right)

        find_sum(root)
        return sum


if __name__ == '__main__':
    input = [10, 5, 15, 3, None, None, 18]
    root = deserialize(input)
    res = Solution().sumOfNodes(root)

    print(f"sum is : {res}")