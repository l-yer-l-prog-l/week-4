def power(a, n):
    n_minus_one = n - 1
    an = a ** n_minus_one
    aa = a * an
    return aa
a = float(input())
n = float(input())
print(power(a, n))
