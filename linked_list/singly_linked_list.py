from node import ListNode


class LinkedList:
    def __init__(self):
        self.head = ListNode(float("inf"))
        self.tail = self.head

    def insert_at_end(self, val):
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def insert_at_beginning(self, val):
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node

    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

    def print(self):
        curr: ListNode = self.head
        while curr:
            print(f"{curr.val} -> ", end="")
            curr = curr.next
        print("None")


linked_list = LinkedList()
for i in range(5):
    linked_list.insert_at_end(i + 1)

linked_list.insert_at_beginning(0)

linked_list.remove(4)
linked_list.print()  # inf -> 0 -> 1 -> 2 -> 3 -> 5 -> None

linked_list.remove(4)
linked_list.print()  # inf -> 0 -> 1 -> 2 -> 3 -> None
