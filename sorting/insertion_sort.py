def insertion_sort(arr):
    """
    Sort an array using the insertion sort algorithm
    Time: O(N*N)
    Space: O(1)

    NOTE:
    - Best case complexity is O(N) i.e. when the array is sorted
    - Worst case complexity is O(N*N) i.e. when the array is sorted but in reverse order
    - Its ideal for small datasets
    """
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -= 1
    return arr


print(
    insertion_sort([10, -1, 2, 3, 0, -11, 11, 111])
)  # [-11, -1, 0, 2, 3, 10, 11, 111]
