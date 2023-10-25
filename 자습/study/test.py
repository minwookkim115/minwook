# def othersSol():
#     a = [None] * 2000001
#     b = map(int, open(0))  # what is open()?
#     next(b)  # what is next()?
#     for i in b: a[i] = 1  # what is b:a[i]=1?
#     print("\n".join(str(i) for i in range(-1000000, 1000001, 1) if a[i]))

b = [0, 0, 5, 57, 4, 9, 10]
a = map(int, input().split())
for _ in range(len(b)):
    print(next(a))