import sys
sys.stdin = open("16904_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    time = [list(map(int, input().split())) for _ in range(N)]
    # time으로 받은 리스트에 뒤에거를 기준으로 정렬
    time.sort(key=lambda x: x[1])
    # 처음하나는 무조건 가능하니까 count = 1
    count = 1
    # 작업 가능한 시간의 인덱스 값
    j = 0
    # 인덱스 i의 시작 시간이
    # 현재 작업하고 있는 j의 끝시간보다 크면
    # 작업가능
    for i in range(N):
        if time[i][0] >= time[j][1]:
            count += 1
            j = i

    print(f"#{tc} {count}")