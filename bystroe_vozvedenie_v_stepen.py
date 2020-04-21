a = float(input())
n = float(input())
if n % 2 == 0:
    asquare = a ** 2
    n0_5 = n / 2
    print(asquare ** n0_5)
else:
    n_minus_one = n - 1
    asqrn = a ** n_minus_one
    print(a * asqrn)
