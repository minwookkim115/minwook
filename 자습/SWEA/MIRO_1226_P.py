import sys

sys.stdin = open("1226_input.txt", "r")

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

T = 10

for tc in range(1, T + 1):
    t = int(input())
    arr = [list(map(int, input())) for _ in range(16)]


    def dsf(r, c, v):

        visited = [[0] * v for _ in range(v)]
        stack = []

        visited[r][c] = 1

        while True:
            answer = 0
            if arr[r][c] == 3:
                answer += 1
                return answer
            for j in range(4):
                nr = r + dr[j]
                nc = c + dc[j]
                if 0 <= nr < v and 0 <= nc < v and arr[nr][nc] != 1 and visited[nr][nc] == 0:
                    stack.append((r, c))
                    visited[nr][nc] = 1
                    r, c, = nr, nc
                    break
            else:
                if stack:
                    r, c = stack.pop()
                else:
                    return 0

    print(f"#{t} {dsf(1, 1, 16)}")
