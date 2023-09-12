import sys

sys.stdin = open("16586_input.txt", "r")


# 재귀함수
# 현재 i번째 행에서 j번째 열을 골라서 합을 만들기
# now_sum = 행을 탐색하면서 현재의 합
def backtraking(i, now_sum):
    # 최소값 수정해야 하니까 global 선언
    global min_v

    # 최적화 조건
    # 현재 내가 알고있는 합이 이전에 구했던 최소 합보다 크면
    # 더 진행할 필요가 있을까?
    # i번째 행까지 구했는데
    # 전에 n번째 행까지 합한 합보다 더 커버리면 이후에 더해봤자
    # 커지면 커졌지 작아지진 않을 것이다... => 가망이 없을 것이다. => return
    if now_sum > min_v:
        return

    # 종료조건
    # i가 몇일때 종료해야할까
    # 최소값 비교는 언제 해야 할까
    if i == N:
        if now_sum < min_v:
            min_v = now_sum
        return

    # 재귀 호출
    # 0 ~ n-1 번째 열 중에서 이전에 고른적이 없는 j열 선택
    for j in range(N):
        # 고른적이 없다면
        if not selected[j]:
            # j번째 열을 골랐다고 체크하고
            selected[j] = 1
            # i+1번째 행에서 몇번째 열을 고를건지 선택하러 gogo
            backtraking(i + 1, now_sum + arr[i][j])
            # 다시 돌아와서 j번째 열을 고르지 않았다고 원복한 뒤에 다음 열에대한 탐색
            selected[j] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행을 기준으로 j번째 열에있는 숫자를 선택했는지 나타내는 배열
    selected = [0] * N
    # 최소값
    min_v = 100

    backtraking(0, 0)

    print(f"#{tc} {min_v}")