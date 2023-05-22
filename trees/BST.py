from utils import *


class TreeNode(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order_traversal(root):
    if not root:
        return

    print(root.val, end=" ")
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)


def in_order_traversal(root):
    if not root:
        return
    in_order_traversal(root.left)
    print(root.val, end=" ")
    in_order_traversal(root.right)


def post_order_traversal(root):
    if not root:
        return
    post_order_traversal(root.left)
    post_order_traversal(root.right)
    print(root.val, end=" ")


def find_min(node):
    while node and node.left:
        node = node.left

    return node.val


def find_max(node):
    while node and node.right:
        node = node.right

    return node.val


def search_node(node, val):

    if node.val == val:
        return True

    if val <= node.val and node.left:
        return search_node(node.left, val)
    elif val >= node.val and node.right:
        return search_node(node.right, val)
    else:
        return False


if __name__ == '__main__':
    input = [10, 5, 15, 3, 7, None, 18]
    tree = deserialize(input)

    # pre_order_traversal(tree)
    # print("\n")
    # in_order_traversal(tree)
    # print("\n")
    post_order_traversal(tree)

    # print(search_node(tree, 18))

    # print(f"sum is : {res}")