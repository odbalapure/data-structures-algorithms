# As the name implies, we go as deep as possible before we bactrack.
# The idea is to pick a direction, say left and keep following pointers
# as far as down left as we can go until we reach "null".
# Once we reach null, we bactrack to the "parent" node and then go right.
# We keep doing this until we have visited every node in the tree.

from node import TreeNode


def inorder(root: TreeNode):
    """
    Inorder traversal of a tree
    Time: O(N)
    Space: O(H)
    """
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


# NOTE: The result be in sorted order, we can create a BST from an array and iterate
# over it get a sorted one and the creation will take O(N * logN) time
if __name__ == "__main__":
    root = TreeNode(4)

    root.left = TreeNode(2)
    root.right = TreeNode(6)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)

    inorder(root)  # 1 2 3 4 5 6 7
