import sys

sys.stdin = open("16883_input.txt", "r")

#    우  하
dr = [0, 1]
dc = [1, 0]


# (0,0)부터 (N-1, N-1)까지 가는 재귀함수
def sum_num(r, c):
    global n_sum # 현재합
    global min_v # 최소합

    if r == c == N - 1: # 오른쪽 끝으로 갔을때
        if min_v > n_sum: # 최소합이 현재합보다 크면
            min_v = n_sum # 최소합으로 교체
        return # 끝내기

    # 우하 돌면서
    for k in range(2):
        nr = r + dr[k]
        nc = c + dc[k]
        # 범위안에 있으면
        if 0 <= nr < N and 0 <= nc < N:
            # 현재 합에 더하고
            n_sum += arr[nr][nc]
            # 재귀 호출
            sum_num(nr, nc)
            # 재귀 하나 끝날때 마다 더해줬던 값 다시 빼주기
            n_sum -= arr[nr][nc]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    n_sum = arr[0][0]
    min_v = 200

    sum_num(0, 0)

    print(f"#{tc} {min_v}")
