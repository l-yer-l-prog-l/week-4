def MinDivisor(n):
    i = 2
    sqrn = n ** 0.5
    while n % i != 0:
        i += 1
        if i > int(sqrn) and sqrn ** 2 == n:
            return n
            pass
        if i >= 50000:
            return n
            pass
    return i


def IsPrime(n):
    return n // MinDivisor(n) == 1
n = int(input())
if IsPrime(n):
    print('YES')
else:
    print('NO')
