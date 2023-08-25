import sys

sys.stdin = open("2819_input.txt", "r")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def is_valid(r, c):
    return 0 <= r < 4 and 0 <= c < 4


def make(r, c, number):
    # 종료조건
    if len(number) == 7:
        numbers.add(number)
        return

    # 재귀호출
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if is_valid(nr, nc):
            make(nr, nc, number + arr[nr][nc])


T = int(input())
for tc in range(1, T + 1):
    arr = [input().split() for _ in range(4)]

    # 내가 만들어본 길을 저장
    numbers = set()

    # 모든 위치 r,c 에서 길을 만들어보기 시작
    for r in range(4):
        for c in range(4):
            make(r, c, arr[r][c])

    print(f"#{tc} {len(numbers)}")
