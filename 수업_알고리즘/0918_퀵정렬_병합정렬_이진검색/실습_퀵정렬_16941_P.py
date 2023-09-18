import sys

sys.stdin = open("16941_input.txt", "r")


def partition(A, l, r):
    # 피벗
    p = A[l]

    # i는 왼쪽에서 시작 피벗보다 큰애들 나오면 멈추고
    # j는 오른쪽에서 시작 피벗보다 작은애들 나오면 멈추고
    # 큰애들은 왼쪽에 있으면 안되고 작은애들은 오른쪽에 있으면 안되니까 서로 바꿔 줄려고
    i = l
    j = r

    # j가 i보다 작아지면 교차하는 지점
    # j랑 피벗이랑 바꿔줘야함
    while i <= j:
        # i가 j 보다 크고
        # i는 큰애들 나오면 멈춰야 하니까 피벗보다 작으면
        while i <= j and A[i] <= p:
            i += 1
        # i가 j 보다 크고
        # i는 작은애들 나오면 멈춰야 하니까 피벗보다 크면
        while i <= j and A[j] >= p:
            j -= 1

        # i가 j보다 작으면
        # 교차하기 전에 바꿔야될 애들 찾음
        if i < j:
            # 바꿔주고
            A[i], A[j] = A[j], A[i]

    # while문 끝난거면 교차 한거
    # 피벗이랑 j랑 바꿔줘야함
    A[l], A[j] = A[j], A[l]

    # 글고 피벗의 인덱스 값 리턴
    return j


def QuickSort(A, l, r):
    # 리스트가 하나 이상일 때만 정렬해야 되니까
    if l < r:
        # 피벗 인덱스
        s = partition(A, l, r)

        # 피벗을 기준으로 왼쪽 정렬
        QuickSort(A, l, s - 1)
        # 피벗을 기준으로 오른쪽 정렬
        QuickSort(A, s + 1, r)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 배열 길이
    A = list(map(int, input().split()))  # 배열

    # 퀵소트 하고
    QuickSort(A, 0, N - 1)
    # A[N//2] 출력
    print(f"#{tc} {A[N // 2]}")
