def f(i, N, s):  # s : i-1원소까지 부분집합의 합(포함된 원소의 합)
    if i == N:
        print(bit, end=" ")
        print(f" : {s}")
        return
    else:
        bit[i] = 1  # 부분집합에 A[i]가 포함
        f(i + 1, N, s + arr[i])
        bit[i] = 0  # 부분집합에 A[i]가 빠짐
        f(i + 1, N, s)
    return


arr = [1, 2, 3]
bit = [0] * 3
f(0, 3, 0)
