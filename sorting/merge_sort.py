def merge_sort(arr, st, end):
    """
    Sort an array using the merge sort algorithm
    Time: O(N * logN)
    Space: O(N)

    NOTE: The complexity remains the same for best, average & worst case
    """
    if st >= end:
        return

    mid = (st + end) // 2

    merge_sort(arr, st, mid)
    merge_sort(arr, mid + 1, end)

    merge(arr, st, mid, end)


def merge(arr, st, mid, end):
    L = arr[st : mid + 1]
    R = arr[mid + 1 : end + 1]

    i, j, k = 0, 0, st

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        k, i = k + 1, i + 1

    while j < len(R):
        arr[k] = R[j]
        k, j = k + 1, j + 1


nums = [3, 1, 2, 5, 4]
merge_sort(nums, 0, len(nums) - 1)
print(nums)
