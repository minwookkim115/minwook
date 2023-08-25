import sys

sys.stdin = open("1979_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # print(N, K)
    # print(puzzle)

    # 들어갈 수 있는 곳 개수
    answer = 0
    # 행 검사
    for r in range(N):
        count = 0  # 칸수 세기
        for c in range(N):
            if puzzle[r][c] == 1:  # 1이면
                count += 1  # count에 + 1씩
            else:  # 0만났을 때
                if count == K:  # K랑 count가 같으면
                    answer += 1  # 들어갈곳 + 1
                count = 0  # count 초기화
        # 0을 만나지 않고 끝났을 때
        if count == K:  # K랑 count가 같으면
            answer += 1  # 들어갈곳 + 1

    # 열검사
    for r in range(N):
        count = 0
        for c in range(N):
            if puzzle[c][r] == 1:
                count += 1
            else:
                if count == K:
                    answer += 1
                count = 0
        if count == K:
            answer += 1

    print(f"#{tc} {answer}")
