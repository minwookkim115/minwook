import sys
sys.stdin = open("1979_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    print(N, K)
    print(puzzle)

    answer = 0
    for r in range(N):
        count = 0
        for c in range(N):
            if puzzle[r][c] == 1:
                count += 1
                