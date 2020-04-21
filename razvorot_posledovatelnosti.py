count = 0
summa = 0
alist = []
while count == 0:
    num = int(input())
    if num != 0:
        alist.insert(0, num)
    else:
        length = len(alist)
        i = 0
        print('0')
        while i < length:
            a = alist[i]
            print(a, end='\n')
            i += 1
        count += 1
