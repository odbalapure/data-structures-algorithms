from node import TreeNode


def search_bst(root: TreeNode, val: int):
    """
    Find a node in BST
    Time: O(H)
    Space: O(H)
    """
    if not root or root.val == val:
        return root
    return search_bst(root.left, val) if val < root.val else search_bst(root.right, val)


def search_bst(root: TreeNode, val: int):
    """
    Find a node in BST
    Time: O(H)
    Space: O(1)
    """
    while root and root.val != val:
        root = root.left if val < root.val else root.right
    return root


root = TreeNode(4)

root.left = TreeNode(2)
root.right = TreeNode(6)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print(search_bst(root, 4))
