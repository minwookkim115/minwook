T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    numbers = list(map(int, input().split()))

    # 최대값 or 최소값의 위치 (인덱스)
    idx = 0

    # 선택 정렬
    for i in range(10):
        # i 위치에 올 원소를 찾아야 합니다.
        max_v = 0
        min_v = 0
        # i 뒤에 있는 원소부터 최댓값 or 최소값 찾기 시작
        for j in range(i, n):
            # i 가 짝수일때 => 최대값
            pass
            # i 가 홀수일때 => 최소값

        # 최대값 or 최소값의 인덱스
        # i 번째 원소는 누가 돼야할까? idx 번째랑 자리를 교환
        pass

    # numbers를 앞에서부터 10개만 출력
