import sys

sys.stdin = open("16586_input.txt", "r")

# 최소값 구하는 함수
def backtraking(i, now_sum):
    global min_v

    if now_sum > min_v: # 현재 합이 최소합보다 크면 안봄
        return

    # 다돌았을 때 최소합이 현재합보다 크면 최소합으로
    if i == N:
        if min_v > now_sum:
            min_v = now_sum
        return

    # j가 N만큼 돌면서
    for j in range(N):
        # 안갔으면
        if selected[j] == 0:
            # 갔다고 표시하고
            selected[j] = 1
            # 다음행에서 열선택
            backtraking(i + 1, now_sum + arr[i][j])
            # 열선택 다 끝나고 했으면 방문한 곳 다시 0으로 하고 탐색
            selected[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    selected = [0] * N
    min_v = 100

    backtraking(0, 0)
    print(f"#{tc} {min_v}")