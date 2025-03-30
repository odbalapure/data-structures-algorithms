def remove_duplicates_brute(nums: list[int]) -> int:
    """
    Remove duplicates from an array
    :param nums: List of integers
    :return: int

    :Time: O(N * logN) | Dominated by sorting the unique elements
    :Space: O(N) | extra space for set and sorted list
    """
    unique: list[int] = sorted(set(nums))
    nums[: len(unique)] = unique
    return len(unique)


def remove_duplicates(nums: list[int]) -> int:
    """
    Remove duplicates from an array
    :param nums: List of integers
    :return: int

    :Time: O(N)
    :Space: O(1)
    """
    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1
    return l


print(remove_duplicates_brute([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
