#AB = √(xb - xa)2 + (yb - ya)2
import math
x1 = float(input("x1 = "))
x2 = float(input("x2 = "))
y1 = float(input("y1 = "))
y2 = float(input("y2 = "))
a = math.sqrt((x2-x1)**2+(y2-y1)**2)
print(f' Расстояние между точками = {a}')
