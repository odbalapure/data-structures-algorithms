def factorial(n):
    """
    Factorial of a number
    Time: O(N)
    Space: O(1)
    """
    res = 1
    while n >= 1:
        res = res * n
        n -= 1
    return res


def factorial(n):
    """
    Factorial of a number
    Time: O(N)
    Space: O(N)
    """
    if n < 1:
        return 1
    return n * factorial(n - 1)


# factorial(4)
# → 4 * factorial(3)
#         ↓
#         3 * factorial(2)
#                 ↓
#                 2 * factorial(1)
#                         ↓
#                         1 * factorial(0)
#                                 ↓
#                                 1   ← Base case returns 1
print(factorial(4))
