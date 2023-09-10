import math

# A = 30
# B = 60
# C = 90

a = 10
b = 11
c = 6


# a**2 = b**2 + c**2 - 2bc * cosA
# A = arccos(b**2 + c**2 - a**2 / 2bc)
num = math.acos((b**2 + c**2 - a**2) / (2*b*c))
A1 = math.degrees(num)
print(A1)

# c**2 = a**2 + b**2 - 2ab * cos다
# 다 = arccos(a**2 + b**2 - c**2 / 2ab)
num1 = math.acos((a**2 + c**2 - b**2) / (2*a*c))
B1 = math.degrees(num1)
print(B1)

num2 = math.acos((a**2 + b**2 - c**2) / (2*a*b))
C1 = math.degrees(num2)
print(C1)

# d**2 = a**2 + (b+2r)**2 - 2*a*(b+2r) * cos다


# (b+2)r**2 = a**2 + d**2 -2ad * cos나
# 나 = a**2 + d**2 - (b+2r)**2 / 2ad

# print(A)