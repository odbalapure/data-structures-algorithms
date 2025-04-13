def bucket_sort(arr):
    """
    Sort an array using the quick sort algorithm
    Time: O(N)
    Space: O(1)
    NOTE: The counts[] size is neligible so the space complexity is O(1)
    """
    counts = [0, 0, 0]
    for num in arr:
        counts[num] += 1

    index = 0
    for i in range(len(counts)):
        for _ in range(counts[i]):
            arr[index] = i
            index += 1

    return arr


print(bucket_sort([2, 1, 2, 0, 0, 2]))
