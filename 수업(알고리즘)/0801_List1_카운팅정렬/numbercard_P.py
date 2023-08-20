# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     numbers = list(map(int, input()))
#
#     mode_arr = [0] * 10
#     mode_num = 0
#     mode_idx = 0
#
#     for i in range(N):
#         mode_arr[numbers[i]] += 1
#
#     for i in range(10):
#         if mode_arr[i] >= mode_num:
#             mode_num = mode_arr[i]
#             mode_idx = i
#
#     print(f"#{tc} {mode_num} {mode_idx}")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = input()

    # 카운트배열 사용 등장하는 숫자의 법위가 0 ~ 9
    # count[i]가 의미하는 것은 numbers에서 숫자 i가 등장한 횟수
    counts = [0] * 10

    for num in numbers:
        counts[int(num)] += 1  # num이 등장한 횟수만큼 1씩 증가

    # 최대 개수
    max_count = 0
    # 가장 큰 수
    max_num = 0

    # 0 ~ 9 까지의 숫자들 중에서 가장 자주 등장한 숫자가 무엇인가?
    # 그리고 등장한 횟수가 같다면 그중에 큰거 골라서 출력

    for i in range(10):
        if counts[i] >= max_count:
            # 숫자 i의 등장 횟수가 지금까지 내가 알고있던 최대 횟수보다 많으면
            # 최대값 갱신
            max_count = counts[i]
            # 최대 등장횟수를 가진 숫자 i 구하기
            max_num = i

    print(f"#{tc} {max_num} {max_count}")