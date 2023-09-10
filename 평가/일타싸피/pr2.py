import math

# A = 30
# B = 60
# C = 90

a = 1
b = float(math.sqrt(3))
c = 2


# a**2 = b**2 + c**2 - 2bc * cosA
# A = arccos(b**2 + c**2 - a**2 / 2bc)
num = math.acos((b**2 + c**2 - a**2) / (2*b*c))
A1 = math.degrees(num)
print(A1)

# c**2 = a**2 + b**2 - 2ab * cos다
# 다 = arccos(a**2 + b**2 - c**2 / 2ab)
num1 = math.acos((a**2 + b**2 - c**2) / 2*a*b)
B1 = math.degrees(num1)
print(B1)

# d**2 = a**2 + (b+2r)**2 - 2*a*(b+2r) * cos다


# (b+2)r**2 = a**2 + d**2 -2ad * cos나
# 나 = a**2 + d**2 - (b+2r)**2 / 2ad

# print(A)