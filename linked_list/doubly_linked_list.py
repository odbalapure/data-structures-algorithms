from node import ListNode


class DoublyLinkedList:
    def __init__(self):
        self.head = ListNode(float("-inf"))
        self.tail = ListNode(float("inf"))
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_front(self, val):
        new_node = ListNode(val)
        new_node.prev = self.head
        new_node.next = self.head.next

        self.head.next.prev = new_node
        self.head.next = new_node

    def insert_end(self, val):
        new_node = ListNode(val)
        new_node.next = self.tail
        new_node.prev = self.tail.prev

        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def remove_front(self):
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

    def remove_end(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    def print(self):
        curr = self.head
        values = []
        while curr:
            values.append(str(curr.val))
            curr = curr.next
        print(" -> ".join(values))


doubly_linked_list = DoublyLinkedList()
for i in range(5):
    doubly_linked_list.insert_end(i + 1)

doubly_linked_list.print()  # -inf -> 1 -> 2 -> 3 -> 4 -> 5 -> inf

doubly_linked_list.remove_front()
doubly_linked_list.print()  # -inf -> 2 -> 3 -> 4 -> 5 -> inf

doubly_linked_list.remove_end()
doubly_linked_list.print()  # -inf -> 2 -> 3 -> 4 -> inf
