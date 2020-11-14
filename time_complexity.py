def int_to_str(i):
    """Time complexity is O(log(i))"""
    if i == 0:
        return '0'
    numbers = '0123456789'
    res = ''
    while i > 0:
        res = numbers[i % 10] + res
        i = i // 10
    return res
