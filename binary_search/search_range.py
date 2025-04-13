def binary_search(arr):
    """
    Binary search based on custom condition
    Time: O(logN)
    Space: O(1)
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if is_correct(mid) > 0:
            right = mid - 1
        elif is_correct(mid) < 0:
            left = mid + 1
        else:
            return mid
    return -1


def is_correct(n):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return 0


print(binary_search([10, 20, 30]))
