import sys

sys.stdin = open("6190_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 숫자 개수
    num_l = list(map(int, input().split()))  # 입력받은 숫자 리스트

    # 단조 없으면 -1 출력
    # 최대값 -1로 초기화
    max_v = -1
    # 입력받는 숫자 돌면서
    for i in range(len(num_l)):
        for k in range(len(num_l)):
            if i == k:
                continue
            else:
                x_val = list(str(num_l[i] * num_l[k]))  # 곱한 값을 문자열 리스트로
                # 곱한 값을 돌면서
                for j in range(len(x_val) - 1):
                    # 단조면
                    if int(x_val[j]) <= int(x_val[j + 1]):
                        # 일단가고
                        continue
                    # 아니면
                    else:
                        # for문 끝
                        break
                # break 안걸린 애들은
                # 단조다
                else:
                    # int로 묶어서
                    x_val_num = int("".join(x_val))
                    # 단조 리스트에 append
                    max_v = max(max_v, x_val_num)

    print(f"#{tc} {max_v}")
