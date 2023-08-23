import sys
sys.stdin = open("1240_input.txt", 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N : 배열의 세로 / M : 배열의 가로

    # 암호 배열
    arr = [list(map(int, input())) for _ in range(N)]

    # break를 위한 변수
    answer = 0
    # 배열에서 따올 코드
    cord = ""
    # 2차원 배열 순회 하면서
    for r in range(N):
        for c in range(M - 1, -1, -1):
            # 1을 만나면
            if arr[r][c] == 1:
                # 56개 가져오고
                for i in range(56):
                    cord += str(arr[r][c - i])
                    # break를 위해 + 1
                    answer += 1
                # for c in range break
                break
        # 56개 됐으면
        if answer == 56:
            # for r in range break
            break

    # 따온코드 뒤집기
    lc = len(cord)
    cl = list(cord)
    for i in range(lc // 2):
        cl[i], cl[lc-1 - i] = cl[lc - 1 - i], cl[i]
    pc = "".join(cl)

    # 7개씩 쪼개기
    bit7 = []
    for i in range(0, 56, 7):
        bit7.append(pc[i: i + 7])

    # 패스워드 규칙
    # 0 ~ 9 까지에 규칙 삽입
    pl = ["0001101", "0011001", "0010011", "0111101", "0100011",
          "0110001", "0101111", "0111011", "0110111", "0001011"]

    # 패스워드에 맞는 규칙 인덱스 값 삽입
    # 인덱스값 == 패스워드 숫자
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