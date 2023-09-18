import sys

sys.stdin = open("16943_input.txt", "r")

L = 0
R = 1

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()

    cnt = 0

    for num in B:
        left = 0
        right = N - 1

        # 기억할 방향, 1 = 오른쪽, 0 = 왼쪽
        dir = -1  # 처음 찾기 시작할 때는 방향 상관 xx

        while left <= right:
            mid = (left + right) // 2

            # 답 찾으면 개수 증가하고 탐색 중단
            if A[mid] == num:
                cnt += 1
                break

            # 답 못찾으면 구역 나누고 진행
            # 내가 찾는게 mid 보다 작으면 왼쪽
            elif num < A[mid]:
                right = mid - 1
                # 왼쪽을 선택했다 라고 기억
                # 내가 이전에 왼쪽을 선택했으면 진행 x
                if dir == L:
                    break

                # 그게 아니면 진행
                dir = L

            # 내가 찾는게 mid보다 크면 오른쪽
            else:
                left = mid + 1

                if dir == R:
                    break

                dir = R

    print(f"#{tc} {cnt}")