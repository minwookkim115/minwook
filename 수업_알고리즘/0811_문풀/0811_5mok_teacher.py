import sys

sys.stdin = open("오목_input.txt", "r")

# 델타배열
# 대각선 포함이라서 8방향 다 봐야 할 것 같지만?
# 4방향만 봐도 된다.
# 오른쪽아래 == 왼쪽 위 // 우 == 좌 // 상 == 하 // 왼쪽아래 == 오른쪽위
dr = [0, 1, 1, 1]
dc = [1, 1, 0, -1]


def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N


def solve():
    # 모든 위치 (r,c)에서 내가 돌('o')을 발견하면
    # 그 돌과 연결된 돌들이 5개가 있는지 확인
    # 5개 있으면 yes
    # 하나도 발견 못하면 No
    for r in range(N):
        for c in range(N):
            # (r,c)에서 돌을 발견 했다.
            if arr[r][c] == "o":
                # 4방향으로 탐색(이어진 돌의 개수 세기)
                for d in range(4):
                    # 오목이니까 한 방향당 5칸씩 가보자
                    for k in range(5):
                        nr = r + dr[d] * k
                        nc = c + dc[d] * k
                        # 다음위치 계산했는데 돌이 아니거나 범위 밖이면 중단
                        if not is_valid(nr, nc) or arr[nr][nc] == ".":
                            break
                    else:
                        # 5번 반복했는데 중간에 break 한적 없으면 돌 5개를 찾았다.
                        return "YES"
    # 함수가 종료되지 않고 여기 까지 실행 된 경우
    # 오목을 찾지 못함
    return "NO"


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 바둑판
    arr = [list(input()) for _ in range(N)]

    # 정답 출력
    print(f"#{tc} {solve()}")
