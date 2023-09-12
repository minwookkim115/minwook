import sys

sys.stdin = open("16903_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N : 컨테이너 수 / M : 트럭 수
    wi = list(map(int, input().split()))  # wi : 컨테이너무게
    ti = list(map(int, input().split()))  # ti : 적재용량

    # 컨테이너 무게와 적재용량 내림차순 정렬
    ti.sort(reverse=True)
    wi.sort(reverse=True)

    # wi와 ti의 인덱스
    i = 0
    j = 0
    # 무게 합
    weight = 0

    while True:
        # wi나 ti 다돌면 끝
        if i == N or j == M:
            break
        # 화물무게가 적재용량보다 적으면
        # 실을수 있으면 운반하고
        if wi[i] <= ti[j]:
            weight += wi[i]
            # 다음거 확인
            i += 1
            j += 1
        # 못실으면
        # 다음 가벼운 화물무게 확인
        else:
            i += 1

    print(f"#{tc} {weight}")
