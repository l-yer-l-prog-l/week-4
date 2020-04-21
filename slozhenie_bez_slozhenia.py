def sum(a, b):
    if a and b >= 0:
        if b == 0:
            return a
        else:
            return sum(a+1, b-1)
    elif a == 0:
        return b
a = int(input())
b = int(input())
print(sum(a, b))
