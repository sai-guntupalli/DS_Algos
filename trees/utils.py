from drawtree import draw_level_order


class TreeNode(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deserialize(input):

    if type(input) == str:
        tree_str = input
        if input == '{}':
            return None
        nodes = [
            None if (val == '#' or val == None) else TreeNode(int(val))
            for val in input.strip('[]{}').split(',')
        ]
    else:
        res = ['#' if ele is None else str(ele) for ele in input]
        tree_str = '[' + ",".join(res) + ']'
        nodes = [None if val == None else TreeNode(int(val)) for val in input]

    print(f"input : {tree_str}\n")
    draw_level_order(tree_str)

    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root