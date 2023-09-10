import math

N = 3
M = 5

def distance(x1, y1, x2, y2):
    dis = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return dis

hole = -1
obj = -1
min = 9999

for i range(N):
    for j range(M):
        tmp = distance(i, j)
        if tmp < min:
            min = tmp
            hole = i
            obj = j

math.sqrt

math.sin

math.atan

math.degrees(radian)
