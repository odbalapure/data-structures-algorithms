from node import TreeNode
from dfs import inorder


def insert(root: TreeNode, val: int):
    """
    Insert a node in a BST
    Time: O(H)
    Space: O(H)

    NOTE:
    - This does not support insertion at non-leaf positions
    - This solution will always insert at leaf node
    """
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


def remove(root: TreeNode, val: int):
    pass


root = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)

insert(root, 5)
inorder(root)
