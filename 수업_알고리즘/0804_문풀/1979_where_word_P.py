T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0  # 단어가 들어갈 수 있는 자리의 수

    for r in range(N):  # 행 우선 순회
        cnt = 0  # 연속한 빈칸(1)의 개수
        for c in range(N):
            if arr[r][c]:  # == 1 이면
                cnt += 1
            if c == N - 1 or arr[r][c] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0

    for c in range(N):  # 열 우선 순회
        cnt = 0  # 연속한 빈칸(1)의 개수
        for r in range(N):
            if arr[r][c]:  # == 1 이면
                cnt += 1
            if r == N - 1 or arr[r][c] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0

    print(f"#{tc} {ans}")