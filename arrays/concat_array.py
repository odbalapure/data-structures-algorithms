def concat_array(nums: list[int]):
    """
    :Time: O(N)
    :Space: O(N)
    """
    ans = []
    for _ in range(2):
        for num in nums:
            ans.append(num)
    return ans


def concat_array(nums: list[int]) -> list[int]:
    """
    :Time: O(N)
    :Space: O(N)
    """
    n = len(nums)
    ans = [0] * (2 * n)
    for i, num in enumerate(nums):
        ans[i] = ans[i + n] = num
    return ans


print(concat_array([1, 2, 1]))  # 1, 2, 1, 1, 2, 1]
