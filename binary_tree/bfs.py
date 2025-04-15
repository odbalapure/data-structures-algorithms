from collections import deque
from node import TreeNode


def bfs(root: TreeNode) -> None:
    """
    BFS traversal of a tree
    Time: O(N)
    Space: O(N)

    NOTE:
    - Time taken is O(N) as each node is visited exactly once
    - Space is O(N) because 1 level is stored at a time,
        last level may be roughly half the size of the tree
    """
    queue = deque()

    if root:
        queue.append(root)

    while len(queue) > 0:
        for _ in range(len(queue)):
            curr = queue.popleft()
            print(curr.val, end=" ")
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)


root = TreeNode(4)

root.left = TreeNode(2)
root.right = TreeNode(6)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

bfs(root)
