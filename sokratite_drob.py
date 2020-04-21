def gsd(a, b):
    i = 0
    while i == 0:
        if a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        else:
            return a + b
            i += 1


def ReduceFraction(n, m):
    gsded = gsd(n, m)
    p = n / gsded
    q = m / gsded
    int(p)
    int(q)
    return p, q
n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
