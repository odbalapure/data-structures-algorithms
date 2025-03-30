def remove_element(nums: list[int], val: int) -> int:
    """
    Remove an input element from the array
    :param nums: List of integers
    :return: int

    :Time: O(N)
    :Space: O(N)
    """
    temp = [num for num in nums if num != val]
    nums[: len(temp)] = temp
    return len(temp)


def remove_element(nums: list[int], val: int) -> int:
    """
    Remove an input element from the array
    :param nums: List of integers
    :return: int

    :Time: O(N)
    :Space: O(1)
    """
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))  # [0,1,3,0,4]
