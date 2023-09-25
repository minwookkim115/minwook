def find_max(r, sub_sum):
    global max_point
    global visited

    # 끝까지 가면
    if r == N:
        # 최대값 찾고
        max_point = max(max_point, sub_sum)
        # 리턴
        return

    # 열을 돌면서
    for c in range(N):
        # 방문 안했으면
        if visited[c] == 0:
            # 방문체크하고
            visited[c] = 1
            # 다음 행으로 가면서 숫자 더하기
            find_max(r + 1, sub_sum + point[r][c])
            # 재귀 끝나면 visited를 0으로 만들고 다음으로 가도록
            visited[c] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 2차원 배열 크기
    point = [list(map(int, input().split())) for _ in range(N)]  # 점수

    # 가장 큰 점수
    max_point = 0
    # 방문한 열을 방문하면 안되기 때문에
    # 방문 배열
    visited = [0] * N

    # 행과 합을 인자로
    find_max(0, 0)

    print(f"#{tc} {max_point}")
