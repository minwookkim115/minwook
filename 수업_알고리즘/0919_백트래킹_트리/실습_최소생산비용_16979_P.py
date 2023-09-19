import sys
sys.stdin = open("16979_input.txt", "r")

# 최소값 찾기
def min_v(row, s):
    # 전역변수 가져와서
    global min_sum

    # 끝나기 전에 s가 min_sum보다 크면 걍 cut
    # 가지치기
    if s >= min_sum:
        return

    # 재귀 다 돌았을 때
    if row == N:
        # 최소값 넣기
        if min_sum >= s:
            min_sum = s
        return

    # N만큼 돌면서
    for i in range(N):
        # 방문 안했으면
        if visited[i] == 0:
            # 방문 표시하고
            visited[i] = 1
            # 재귀 들어감
            min_v(row + 1, s + V[row][i])
            # 재귀 나올 때 다음 값을 위해서
            # 방문 다시 0으로
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 2000
    visited = [0] * N

    min_v(0, 0)

    print(f"#{tc} {min_sum}")