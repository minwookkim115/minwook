import sys

sys.stdin = open("2805_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 농장 크기
    garden = [list(map(int, input())) for _ in range(N)] # 농장 받고

    # 모두 더한 값
    max_get = 0
    # N을 2로 나눈 몫
    c = N // 2

    # 행을 반만 위에서 아래로 돌면서
    for r in range(c + 1):
        # 한 행의 합
        get = 0
        # 첫번째 행은
        if r == 0:
            # 그냥 가운데 더해주고
            max_get += garden[r][c]
        # 다음 행부터
        else:
            # 가운데 더해주고
            max_get += garden[r][c]
            # 1씩 늘어나면서
            for k in range(1, r + 1):
                # 행의합에 더하고
                get += garden[r][c - k] + garden[r][c + k]
            # 모두 더한 값에 더해주기
            max_get += get

    # 행 밑에서부터 올라오면서
    # 가운데는 안가고
    for r in range(N-1, c, -1):
        # 한 행의 합
        get = 0
        # 제일 마지막 행은
        if r == N-1:
            # 그냥 가운데 더해주고
            max_get += garden[r][c]
        # 다음행으로 올라가면서
        else:
            # 모든 합에 가운데 더해주고
            max_get += garden[r][c]
            # 1씩 증가하면서
            for k in range(1, ((N-1) - r) + 1):
                # 행의 합에 더해주고
                get += garden[r][c - k] + garden[r][c + k]
            # 모든합에 더하기
            max_get += get

    print(f"#{tc} {max_get}")
