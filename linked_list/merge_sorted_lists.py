from .linked_list import ListNode


def merge_list(list1: ListNode, list2: ListNode) -> ListNode:
    """
    Merge 2 sorted linked lists
    :param list1: Head of linked list 1
    :param list2: Head of linked list 2
    :return: ListNode

    :Time: O(M + N)
    :Space: O(1)
    """
    dummy = node = ListNode()

    while list1 and list2:
        if list1.val <= list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next
        node = node.next

    node.next = list1 or list2

    return dummy.next


def merge_list(list1: ListNode, list2: ListNode) -> ListNode:
    """
    Merge 2 sorted linked lists
    :param list1: Head of linked list 1
    :param list2: Head of linked list 2
    :return: ListNode

    :Time: O(M + N)
    :Space: O(M + N)
    """
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1.val <= list2.val:
        list1.next = merge_list(list1.next, list2)
        return list1
    else:
        list2.next = merge_list(list1, list2.next)
        return list2
