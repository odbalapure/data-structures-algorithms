class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = ListNode(float("-inf"))
        self.tail = self.head

    def enqueue(self, val):
        """
        Append element at the end of a queue
        Time: O(1)
        """
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def deque(self):
        """
        Pop element from the beginning of a queue
        Time: O(1)
        """
        if not self.head.next:
            return None

        val = self.head.next.next
        self.head.next = self.head.next.next

        if not self.head.next:
            self.tail = self.head

        return val

    def print(self):
        curr = self.head.next
        while curr:
            print(f"{curr.val} -> ", end="")
            curr = curr.next
        print("None")


queue = Queue()
for i in range(5):
    queue.enqueue(i + 1)

queue.print()  # 1 -> 2 -> 3 -> 4 -> 5 -> None

queue.deque()
queue.print()  # 1 -> 2 -> 3 -> 4 -> None

queue.enqueue(100)
queue.deque()
queue.print()  # 3 -> 4 -> 100 -> None
