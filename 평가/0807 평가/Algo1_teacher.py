import sys
sys.stdin = open("algo1_sample_in.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    r1, c1, r2, c2 = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1. 평균을 구하기 위해서 총합, 영역의 칸수(넓이)를 알아야 한다.
    sumV = 0  # 총합
    cnt = 0  # 영역의 칸수
    # (r1-r1+1) * (c2-c2+1) 영역 넓이

    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            sumV += arr[r][c]
            cnt += 1

    # 평균값 구하기
    avgV = sumV // cnt

    # 총 작업 횟수
    result = 0
    # 2. 작업 회수를 센다.
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            # 작업 횟수 구하는 방법
            # 현재 (r,c) 위치의 높이 - 평균값의 절대값
            sub = arr[r][c] - avgV
            if sub < 0:
                sub = -sub

            result += sub

    # 정답 출력
    print(f"#{tc} {result}")