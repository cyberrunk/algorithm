def recursion_multiply(a, b):
    if b == 1:
        return a
    return a + recursion_multiply(a, b - 1)


def recursion_factorial(n):
    if n == 1:
        return 1
    return n * recursion_factorial(n - 1)


def towers(n, fr, to, spare, k):
    if n == 1:
        print_move(fr, to, k)
    else:
        towers(n - 1, fr, spare, to, k + 1)
        towers(1, fr, to, spare, k + 1)
        towers(n - 1, spare, to, fr, k + 1)


def print_move(fr, to, k):
    print('move form', fr, 'to', to, k)

