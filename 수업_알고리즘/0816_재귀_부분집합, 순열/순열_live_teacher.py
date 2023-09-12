def f(i, N):
    if i == N:
        print(f"answer{A}")
    else:
        for j in range(i, N):
            A[i], A[j] = A[j], A[i] # 자신부터 오른쪽 끝까지
            print(f"1 : {i},{j} {A}")
            f(i + 1, N)
            A[i], A[j] = A[j], A[i] # 원상복구해서 오른쪽이랑 바까볼까
            print(f"2 : {i},{j} {A}")

A = [1, 2, 3]
f(0, 3)
