def nCr(n, r, s):
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n - r + 1):
            comb[r - 1] = A[i]
            nCr(n, r - 1, s + 1)


A = [1, 2, 3, 4, 5, 6]
N = len(A)
R = 3
comb = [0] * R
nCr(N, R, 0)
