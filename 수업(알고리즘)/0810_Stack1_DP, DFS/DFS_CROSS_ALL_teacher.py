dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 0이 이동할 수 있는 칸
# 1이 이동할 수 없는 벽
# 3은 도착점
arr = [[0, 0, 0, 0, 1, 3],
       [1, 1, 0, 0, 1, 0],
       [0, 0, 0, 0, 1, 0],
       [0, 1, 0, 0, 1, 0],
       [0, 1, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0]]


# dfs로 2차원 배열 순회하기
# 인접한 정점 == 상하좌우
# 시작 행 번호 : r
# 시작 열 번호 : c
# 한 변의 길이 : n

def dfs(r, c, n):
    # 방문체크 배열
    visited = [[0] * n for _ in range(n)]
    # visited[i][j] == 1 : (i,j) 위치를 방문한 적이 있다.
    # visited[i][j] == 0 : (i,j) 위치를 방문한 적이 없다.
    stack = []
    # 시작 위치 표시
    visited[r][c] = 1

    while True:

        for i in range(n):
            for j in range(n):
                if (i, j) == (r, c):
                    print("*", end=" ")
                else:
                    print(arr[i][j], end=" ")
            print()
        print("============================")
        # 현재위치가 도착지점인지 확인
        if arr[r][c] == 3:
            print("도착")
            break
        # 현재위치 (r,c)에서 다음 위치로 갈 수 있나 확인
        # 상하좌우로 움직일 수 있나 확인, 움직일 수 있으면 가자
        for d in range(4):
            # 다음 위치 계산
            nr = r + dr[d]
            nc = c + dc[d]
            # 계산 후에 (nr, nc)가 갈수 있는 곳인지 확인
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and arr[nr][nc] != 1:
                # (nr, nc) 위치로 갈수 있다고 확인
                # 돌아올 위치를 스택에 저장(현재 위치)
                stack.append((r, c))
                # 방문 체크
                visited[nr][nc] = 1
                # (nr, nc)를 현재위치로 변경
                r, c = nr, nc
                # 이전에 탐색하고 있던 r, c
                # 새로운 위치에서 탐색을 하기 위해서
                break
        # 4 방향을 모두 봤는데 갈 수 있는 곳이 없다.
        else:
            # 내가 전에 저장해 놨던 최근 위치로 돌아가기
            if stack:
                r, c = stack.pop()
            else:
                break


dfs(0, 0, 6)
