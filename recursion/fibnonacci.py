def fibonacci(n):
    """
    Find Nth fibnoacci number
    Time: O(N)
    Space: O(1)
    """
    if n <= 1:
        return n

    n0, n1 = 0, 1
    for _ in range(2, n + 1):
        n0, n1 = n1, n0 + n1

    return n1


def fibonacci(n):
    """
    Find Nth fibnoacci number
    Time: O(2^N)
    Space: O(N)
    """
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
