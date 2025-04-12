def bubble_sort(arr):
    """
    Sort an array using the bubble sort algorithm
    Time: O(N * N)
    Space: O(1)

    NOTE:
    - Best case complexity is O(N) i.e. when the array is sorted
    - Worst and average case complexity is O(N * N)
    """
    for i in range(len(arr)):
        is_swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swapped = True
        if not is_swapped:
            break
    return arr


print(bubble_sort([10, -1, 2, 3, 0, -11, 11, 111]))  # [-11, -1, 0, 2, 3, 10, 11, 111]
print(bubble_sort([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(bubble_sort([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]
