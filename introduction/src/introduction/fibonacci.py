def compute_fibonacci(n):
    """Return the nth Fibonacci number.

    >>> compute_fibonacci(0)
    0
    >>> compute_fibonacci(1)
    1
    >>> compute_fibonacci(2)  # 0 + 1
    1
    >>> compute_fibonacci(3)  # 1 + 1
    2
    >>> compute_fibonacci(4)  # 1 + 2
    3
    """
    # BEGIN QUESTION 1.1
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr
    # END QUESTION 1.1
