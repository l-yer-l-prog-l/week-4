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
a = int(input())
b = int(input())
print(gsd(a, b))
