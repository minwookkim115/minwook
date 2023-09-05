import sys

sys.stdin = open("1244_input.txt", "r")


def swap(cnt, c):
    global max_v
    # 종료 조건 : 교환 횟수를 다 소모 했다면
    # 바꾼 결과물을 숫자로 바꿔서 최대상금 계산
    if cnt == N:
        a = ""
        for i in S:
            a += i
        if max_v < int(a):
            max_v = int(a)
        return

    # 자리를 바꿀 위치 2개를 교환 한번 할때마다 새로 지정
    # 이 문제에서는 동일한 위치에서 중복 교환을 허용
    # 바꿀 위치중에 앞쪽: i
    # 바꿀 위치중에 뒤쪽: j
    for i in range(len(S) - 1):
        for j in range(i + 1, len(S)):
            S[i], S[j] = S[j], S[i]
            if S[0] == max(S):
                swap(cnt + 1, c)
                # 바꿨던거 원상 복구 시키고 새로운 i, j 지정
                S[i], S[j] = S[j], S[i]
            else:
                S[i], S[j] = S[j], S[i]


T = int(input())
for tc in range(1, T + 1):
<<<<<<< HEAD
    num, c = map(int, input().split())
=======
    S, N = input().split()
    S = list(S)
    N = int(N)
    max_v = 0
    check = []

    swap(0, check)

    print(f"#{tc} {max_v}")
>>>>>>> 48beb20a8605c14a15f8e56ad4b07d4274b49bdd
