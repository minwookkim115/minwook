import sys
sys.stdin = open("16786_input.txt", "r")


T = int(input())
for tc in range(1, T + 1):
    N, sixteen = input().split()

    # 2진수로 변환
    two = ""

    # N만큼 돌면서
    for i in range(int(N)):
        # 16 진수를 10진수로 바꾼 수
        dec = int(sixteen[i], 16)
        # 8이상이면 1 추가하고 8 빼고
        if dec >= 8:
            two += "1"
            dec -= 8
        # 아니면 0 추가
        else:
            two += "0"
        # 뺀수가 4 이상이면 1 추가하고 4 빼고
        if dec >= 4:
            two += "1"
            dec -= 4
        # 아니면 0 추가
        else:
            two += "0"
        # 뺀수가 2 이상이면 1 추가하고 2 빼고
        if dec >= 2:
            two += "1"
            dec -= 2
        # 아니면 0 추가
        else:
            two += "0"
        # 1이 남았으면 1 추가하고
        if dec == 1:
            two += "1"
        # 아니면 0 추가
        else:
            two += "0"

    print(f"#{tc} {two}")