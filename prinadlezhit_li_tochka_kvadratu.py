def IsPointInSquare(x, y):
    return(-1 <= x <= 1 and -1 <= y <= 1)
pointX = float(input())
pointY = float(input())
func = IsPointInSquare(pointX, pointY)
if func:
    print('YES')
else:
    print('NO')
