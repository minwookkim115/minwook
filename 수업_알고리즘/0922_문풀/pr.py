import sys

sys.stdin = open("5656_input.txt")

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())


# 내가 지금까지 공을 떨어뜨린 횟수 : n
# 현재 벽돌들의 상태 정보 : bricks (2차원 배열)
# 현재 남은 벽돌의 개수 : remain
def pick(n, bricks, remain):
    global answer

    # n번 공을 떨어뜨림 (공을 떨어뜨릴 위치를 n번 고름)
    # 또는 남은 벽돌의 개수가 0이니까 더이상 진행할 필요 x
    if n == N or remain == 0:
        cnt = 0
        for r in range(H):
            for c in range(W):
                if bricks[r][c]:
                    cnt += 1

        answer = min(answer, cnt)

        return

    # 0 ~ W-1
    for c in range(W):
        # c 번 열에서 공을 떨어뜨려 보기
        # 공을 한번 떨굴때마다 벽돌의 상태가 변해야 하므로
        # deepcopy해서 각 상태 유지
        now_bricks = [[bricks[i][j] for j in range(W)] for i in range(H)]

        # BFS로 상하좌우 터지는것 구현
        q = deque()

        # 위에서부터 벽돌 찾기
        for r in range(H):
            if now_bricks[r][c]:
                # 터지기 시작하는 벽돌의 위치와, 퍼져나가는 범위
                q.append((r, c, now_bricks[r][c]))
                now_bricks[r][c] = 0  # 쾅
                break  # 밑에 벽돌은 아직 터뜨리면 안돼

        # 벽돌 없으면 안터뜨려도 됨, 건너뛰기
        if not q:
            continue

        # 벽돌 부수기 시작

        # 부순 벽돌의 개수
        b_cnt = 0

        # BFS , 벽돌 부순다.
        while q:
            # i : 벽돌 행번호, j : 벽돌 열번호
            # k : 벽돌에 적힌 숫자 (파괴 범위)
            i, j, k = q.popleft()
            b_cnt += 1  # 벽돌 하나 깨짐

            # 상하좌우 퍼져나가기
            for l in range(1, k):
                for d in range(4):
                    ni = i + dr[d] * l
                    nj = j + dc[d] * l
                    if 0 <= ni < H and 0 <= nj < W and now_bricks[ni][nj]:
                        # 벽돌에 적힌 숫자가 1보다 큰 경우만 큐에 삽입
                        # 벽돌에 적힌 숫자가 1이하이면 퍼져나가지 않음
                        if now_bricks[ni][nj] > 1:
                            q.append((ni, nj, now_bricks[ni][nj]))
                        now_bricks[ni][nj] = 0  # 쾅

        # 벽돌 다 부수고 나면 빈공간 정리
        for j in range(W):
            # 밑에서부터 0인부분 찾고 거기서부터 땡겨오기
            for i in range(H - 1, -1, -1):
                if not now_bricks[i][j]:
                    # 0 인부분 찾았는지
                    find = True
                    # i-1 부터 벽돌이 있는곳 찾기 시작
                    for ni in range(i - 1, -1, -1):
                        if now_bricks[ni][j]:
                            find = True
                            now_bricks[i][j] = now_bricks[ni][j]
                            now_bricks[ni][j] = 0
                            break
                    # 위에 벽돌이 없었으면 더이상 정리 x
                    if not find:
                        break

        # 내가 부순만큼 남은 벽돌 개수 감소
        pick(n + 1, now_bricks, remain - b_cnt)


for tc in range(1, T + 1):
    # N : 드랍 횟수
    # W : 가로, H : 세로
    N, W, H = map(int, input().split())

    # 벽돌 정보
    bricks = [list(map(int, input().split())) for _ in range(H)]

    # 남은 벽돌의 개수의 최소값
    answer = W * H * 10

    # 남은 벽돌의 개수 => 0이 되면 더 구슬을 드랍할 필요가 없음
    remain = 0
    for r in range(H):
        for c in range(W):
            if bricks[r][c]:
                remain += 1

    # 재귀 함수
    # 0번 골랐고, 현재 벽돌의 상태, 남은 벽돌의 개수
    pick(0, bricks, remain)

    print(f"#{tc} {answer}")