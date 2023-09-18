import sys

sys.stdin = open("16943_input.txt", "r")


def binarySearch(l, r, target, left, right):
    global count
    # 왼쪽한번 오른쪽 한번 가야되는데
    # 왼쪽이나 오른쪽 두번가면
    # 끝내버리기
    if abs(left - right) == 2:
        return

    # 찾는 값이 없을 경우
    if l > r:
        return

    # 중간값 구하기
    m = (l + r) // 2

    # 찾았으면 count + 1
    if target == A[m]:
        count += 1
        return
    # 타겟이 더크면 오른쪽으로 가야하니까 right에 + 1
    elif A[m] < target:
        if left == 1:
            return binarySearch(m + 1, r, target, left - 1, right + 1)
        else:
            return binarySearch(m + 1, r, target, left, right + 1)
    # 타겟이 더 작으면 왼쪽으로 가야하니까 left에 + 1
    else:
        if right == 1:
            return binarySearch(l, m - 1, target, left + 1, right - 1)
        else:
            return binarySearch(l, m - 1, target, left + 1, right)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    count = 0  # 왔다리 갔다리 하는거 세기

    for i in B:
        binarySearch(0, N - 1, i, 0, 0)

    print(f"#{tc} {count}")
