T = int(input())    # 테스트케이스 개수
for tc in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))   # split 하면 띄어쓰기를 기준으로 input / map 은 각각 하나씩
    max_v = arr[0]  # 초기값 설정
    min_v = arr[0]  # 초기값 설정
    for i in range(1, N):
        if max_v < arr[i]:
            max_v = arr[i]
        if min_v > arr[i]:
            min_v = arr[i]

    ans = max_v - min_v
    print(f"#{tc} {ans}")
