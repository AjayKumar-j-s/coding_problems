def divide(dividend, divisor):
    f = 0
    if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
        f = 1
    dividend = abs(dividend)
    divisor = abs(divisor)
    q = 0
    while (True):
        if (dividend - divisor >= 0):
            q += 1
        else:
            return q if f else -q
        dividend -= divisor


a = -2147483648
b = -1
print(divide(a, b))