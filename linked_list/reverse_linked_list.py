from node import ListNode


def reverse(head: ListNode) -> ListNode:
    """
    Reverse a linked list
    :param head: Head of linked list
    :return: ListNode

    :Time: O(N)
    :Space: O(1)
    """
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def reverse(head: ListNode) -> ListNode:
    """
    Reverse a linked list
    :param head: Head of linked list
    :return: ListNode

    :Time: O(N)
    :Space: O(N)
    """
    if not head:
        return None

    newHead = head
    if head.next:
        newHead = reverse(head.next)
        head.next.next = head
    head.next = None

    return newHead
