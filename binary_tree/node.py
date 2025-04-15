class TreeNode:
    # Height: measured from a node down to its deepest leaf node
    # Depth: measured from a node up to the root node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def min_node(root: TreeNode):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr
