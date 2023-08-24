import sys
sys.stdin = open("1242_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input()[:M] for _ in range(N)]

    # print(arr)
    arr1 = ["" for _ in range(N)]
    for r in range(N):
        for c in range(M):
            dec = int(arr[r][c], 16)
            for i in range(3, -1, -1):
                if dec & (1 << i) == 0:
                    arr1[r] += "0"
                else:
                    arr1[r] += "1"

    print(arr1)
    arr1_l = len(arr1[0])
    # print(arr1_l)
    code = ""
    answer = 0
    for r in range(N):
        for c in range(arr1_l-1, -1, -1):
            if arr1[r][c] == "1":
                for i in range(56):
                    code += arr1[r][c - i]
                    answer += 1
                break
        if answer == 56:
            break
    print(code)

    # 따온코드 뒤집기
    lc = len(code)
    cl = list(code)
    for i in range(lc // 2):
        cl[i], cl[lc-1 - i] = cl[lc - 1 - i], cl[i]
    pc = "".join(cl)
    print(pc)

    bit7 = []
    for i in range(0, 56, 7):
        bit7.append(pc[i: i + 7])
    print(bit7)

    pl = ["3211", "2221", "2122", "1411", "1132",
          "1231", "1114", "1312", "1213", "3112"]

    password = []
    for i in bit7:
        for j in range(len(pl)):
            if i == pl[j]:
                password.append(j)

    # 짝수 합
    jsum = 0
    # 홀수 합
    hsum = 0
    for i in range(len(password)):
        if i % 2 == 0:
            hsum += password[i]
        else:
            jsum += password[i]

    # 결과 구하기
    result = 0
    # 올바른 암호 코드면
    # 결과에 더하기
    if (hsum * 3 + jsum) % 10 == 0:
        for i in password:
            result += i
    # 틀린 코드면 0 출력
    else:
        result = 0

    print(f"#{tc} {result}")