def bisection_cube(n):
    """calculate cube using bisection"""
    count = 0
    low = 0.0
    epsilon = 0.000000000000001
    high = n
    if n < 1:
        high = 1
        low = n
    guess = (low + high) / 2.0
    while abs(guess ** 3 - n) > epsilon:
        count += 1
        if guess ** 3 > n:
            high = guess
        else:
            low = guess
        guess = (high + low) / 2.0
    return guess


def bisection_search(l, e):
    """l should be a sorted list"""

    def bisection_search_helper(l, e, low, high):
        if high == low:
            return l[low] == e
        mid = (low + high) // 2
        if l[mid] == e:
            return True
        elif l[mid] > e:
            if low == mid:
                return False
            else:
                return bisection_search_helper(l, e, low, mid - 1)
        else:
            return bisection_search_helper(l, e, mid + 1, high)

    if len(l) == 0:
        return False
    else:
        return bisection_search_helper(l, e, 0, len(l) - 1)
