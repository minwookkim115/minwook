# def othersSol():
#     a = [None] * 2000001
#     b = map(int, open(0))  # what is open()?
#     next(b)  # what is next()?
#     for i in b: a[i] = 1  # what is b:a[i]=1?
#     print("\n".join(str(i) for i in range(-1000000, 1000001, 1) if a[i]))

# b = [0, 0, 5, 57, 4, 9, 10]
# a = map(int, input().split())
# for _ in range(len(b)):
#     print(next(a))

import random
a = list(range(1, 46))
b = [1, 4, 9, 24, 37, 42, 45, 6, 13, 32, 12, 34,
     43, 22, 26, 31, 5, 14, 15, 18, 29, 44, 3, 27, 35, 2, 16, 28,
     17, 20, 40, 7, 25, 10, 33]
c = set(a) - set(b)
c = list(c)
print([4, 37, 42, 17, *sorted(random.sample(c, 2))])

# 4, 37, 42