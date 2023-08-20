T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_v_list = []
    min_v_list = []

    for i in range(N):
        if arr[i]:
            pass