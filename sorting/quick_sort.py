def quick_sort(arr, st, end):
    """
    Sort an array using the quick sort algorithm
    Time: O(N * logN)
    Space: O(N)

    NOTE: Its an unstable algorithm, the worst case time complexity will be O(N * N)
    """
    if st >= end:
        return

    left = st
    pivot = arr[end]

    for i in range(st, end):
        if arr[i] < pivot:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1

    arr[end] = arr[left]
    arr[left] = pivot

    quick_sort(arr, st, left - 1)
    quick_sort(arr, left + 1, end)


nums = [3, 1, 2, 5, 4]
quick_sort(nums, 0, len(nums) - 1)  # [1, 2, 3, 4, 5]
print(nums)

nums = [7, 3, 7, 4, 5]
quick_sort(nums, 0, len(nums) - 1)  # [3, 4, 5, 7, 7]
print(nums)
