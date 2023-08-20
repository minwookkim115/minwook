def counting_sort_asc(A, B, K):
    C = [0] * (K + 1)

    print(A)

    for i in range(len(A)):
        C[A[i]] += 1

    print(C)

    # for i in range(1, len(C)):
    #     C[i] += C[i - 1]

    for i in range(len(C)-2, -1, -1):
        C[i] += C[i + 1]

    print(C)

    for i in range(len(B) - 1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]


nums = [0, 4, 1, 3, 1, 2, 4, 1]

result_asc = [0] * 8

counting_sort_asc(nums, result_asc, max(nums))

print(result_asc)
