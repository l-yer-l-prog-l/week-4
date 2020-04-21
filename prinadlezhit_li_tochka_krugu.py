def IsPointInCircle(x, y, xc, yc, r):
    newxc = xc - xc
    newyc = yc - yc
    newx = x - xc
    newy = y - yc
    sqrr = r ** 2
    sqrnewx = newx ** 2
    sqrnewy = newy ** 2
    if sqrnewx + sqrnewy <= sqrr:
        return 'YES'
    else:
        return 'NO'
pointX = float(input())
pointY = float(input())
centerX = float(input())
centerY = float(input())
radius = float(input())
func = IsPointInCircle(pointX, pointY, centerX, centerY, radius)
print(func)
