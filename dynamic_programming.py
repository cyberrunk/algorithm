def fib(n):
    """regular recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        k = fib(n - 1) + fib(n - 2)
    return k


def fast_fib(n, d={}):
    """dynamic programming optimization"""
    if n == 0 or n == 1:
        d[n] = 1
    else:
        try:
            d[n] = d[n - 1] + d[n - 2]
        except KeyError:
            d[n] = fast_fib(n - 1, d) + fast_fib(n - 2, d)
    return d[n]


def simple_fib(n):
    """very simple approach using loop"""
    n0 = 1
    n1 = 1
    for num in range(2, n + 1):
        result = n0 + n1
        n0 = n1
        n1 = result
    return result
