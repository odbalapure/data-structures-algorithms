def binary_search(arr, target):
    """
    Search an element using binary search
    Time: O(logN)
    Space: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            return mid
    return -1


print(binary_search([1, 2, 3, 4, 5, 6], 3))  # 2
