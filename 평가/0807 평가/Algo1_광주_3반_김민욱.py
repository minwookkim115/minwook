import sys
sys.stdin = open("algo1_sample_in.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 마당 크기
    r1, c1, r2, c2 = map(int, input().split())  # 평탄화 할 마당 좌표
    land = [list(map(int, input().split())) for _ in range(N)]  # 마당

    land_sum = 0  # 평탄화 할 땅의 높이 합
    land_width = ((r2 + 1) - r1) * ((c2 + 1) - c1)  # 평탄화 할 땅의 넓이

    for r in range(r1, r2 + 1):  # 평탄화할 마당의 행 좌표
        for c in range(c1, c2 + 1):  # 평탄화할 마당의 열 좌표
            land_sum += land[r][c]

    count = 0

    i = 0

    while i < 101:  # i의 최대값 까지 반복
        for r in range(r1, r2 + 1):  # 평탄화할 마당의 행 좌표
            for c in range(c1, c2 + 1):  # 평탄화할 마당의 열 좌표
                if land[r][c] > (land_sum // land_width):  # 평균보다 크면
                    land[r][c] -= 1  # 평탄화 -1 하고
                    count += 1  # 횟수 + 1
                    continue  # 한번하고 끝나면 안되니까 평균이랑 같을때 까지 반복
                if land[r][c] < (land_sum // land_width):  # 평균보다 작으면
                    land[r][c] += 1  # 평탄화 + 1 하고
                    count += 1  # 횟수 + 1
                    continue  # 한번하고 끝나면 안되니까 평균이랑 같을때 까지 반복

        i += 1

    print(f"#{tc}", count)
