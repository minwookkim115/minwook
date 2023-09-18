import sys

sys.stdin = open("1486_input.txt", "r")


# 부분집합 구하기
# i는 0부터 시작, N 만큼
def find(i, N):
    # i가 N이랑 같으면
    # 부분집합 하나 만들어짐
    if i == N:
        height = 0  # 높이 합
        for j in range(N):  # j가 N만큼 돌면서
            if bit[j]:  # bit[j]가 1이면 (부분집합에 해당)
                height += Hi[j]  # Hi에 부분집합만큼 더하기
        # 더한 값이 B보다 크면
        if height >= B:
            # 리스트에 추가
            over_list.append(height)
            return
    # i가 N까지 못가면
    # bit배열을 1과 0으로 바꾸는 재귀를 돌면서
    # i가 N까지 갈 수 있도록
    else:
        bit[i] = 1
        find(i + 1, N)
        bit[i] = 0
        find(i + 1, N)
    return


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    Hi = list(map(int, input().split()))

    bit = [0] * N
    over_list = []
    find(0, N)

    print(f"#{tc} {min(over_list) - B}")
