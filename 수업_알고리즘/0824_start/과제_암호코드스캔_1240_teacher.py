# import sys
import sys
sys.stdin = open("1242_input.txt", "r")

decrypt = {(2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4,
           (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9}

# sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())

    dup_check = []
    result = 0

    # 각 줄에 대해서 중복 처리 하기
    arr = (list(set([input()[:m] for _ in range(n)])))

    # 줄 검사
    for i in range(len(arr)):
        row = arr[i]

        # 16진수 2진수로 바꾸기
        bin_row = ""
        for char in row:
            # 글자 하나 떼서 16진수
            c_hex = int(char, 16)
            # 16진수는 이진수 * 4
            for j in range(3, -1, -1):
                bin_row += "1" if c_hex & (1 << j) else "0"

        #  바꿨는데 1이 없다? 다 0이니까 코드가 없는것이다.
        if "1" not in bin_row:
            # 다음 줄로 이동
            continue
        else:
            ratio = [0] * 4  # 0 과 1의 비율
            # 0 1 0 1 순서로 번갈아 가면서 나온다.
            # 코드표를 보면, 비율이 각각 유니크함.
            # 어차피 모든 코드는 마지막이 1로 끝나니까 오른쪽 0은 잘라버리자.
            bin_row = bin_row.rstrip("0")
            # print(bin_row)
            new_code = []
            # 맨끝이 1이니까 뒤부터 세기
            for j in range(len(bin_row) - 1, -1, -1):
                if bin_row[j] == "1" and ratio[2] == 0:  # 마지막 1 세기
                    ratio[3] += 1
                elif bin_row[j] == "0" and ratio[1] == 0:  # 세번째 0 세기
                    ratio[2] += 1
                elif bin_row[j] == "1" and ratio[0] == 0:  # 두번째 1 세기
                    ratio[1] += 1
                elif bin_row[j] == "0" and bin_row[j - 1] == "1":
                    # 다음에 나오는 첫번째 0을 제외한 이진수들 숫자를 모두 셌으니 비율 계산 시작
                    # print(ratio)
                    # 같은 비율로 늘어나니까 제일 작은 수를 구해서 나눠버리자
                    min_ratio = min(ratio[1:4])
                    number = decrypt[(ratio[1] // min_ratio, ratio[2] // min_ratio, ratio[3] // min_ratio)]
                    # 비율 다 계산 했으니 초기화, 한 줄에 다른 코드뭉치가 있을수도 있음.
                    ratio = [0] * 4
                    # print(ratio)
                    # 코드에 해당하는 숫자를 구해서 새로운 코드 만들기, 주의할점은 뒤부터 만들었다는것
                    # 0 1 2 3 4 5 6 7
                    # 8 7 6 5 4 3 2 1
                    new_code.append(number)
                    # 코드 길이가 8인지
                    if len(new_code) == 8:
                        odd = new_code[1] + new_code[3] + new_code[5] + new_code[7]
                        even = new_code[0] + new_code[2] + new_code[4] + new_code[6]
                        if (odd * 3 + even) % 10 == 0 and new_code not in dup_check:
                            # 검증 결과 10으로 나누어 떨어지면 올바른 코드
                            # 각 자리수를 더해서 저장한다. (짝수 + 홀수)
                            result += odd + even
                            # 중복 처리
                            dup_check.append(new_code)
                            # print(dup_check)
                        new_code = []  # 마찬가지로 다른 코드 뭉치가 있을수도 있으니 초기화

    print(f"#{tc} {result}")