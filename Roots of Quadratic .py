a = int(input())
b = int(input())
c = int(input())

import math

if b * b - 4 * a * c > 0:
    print("two root", (-b +(math.sqrt((b * b) - 4 * a * c))) / 2 * a, (-b -(math.sqrt((b * b) - 4 * a * c))) / 2 * a)
elif b * b - 4 * a * c == 0:
    print("one root", (-b +(math.sqrt((b * b) - 4 * a * c))) / 2 * a)
else:
    print("no root")