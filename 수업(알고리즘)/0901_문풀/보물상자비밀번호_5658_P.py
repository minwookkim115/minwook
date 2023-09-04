import sys

sys.stdin = open("5658_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    hx = input()

    # 원형큐 느낌으로 돌릴려고
    # N//4 만큼 돌리면 다돌린거니까
    # 앞에다가 N//4 만큼 넣어두고
    q = [0] * (N//4) + [0] * N

    # 일단 하나씩 집어넣고
    for i in range(len(hx)):
        q[i + (N//4)] = hx[i]

    a = 0
    num_s = set()
    while True:
        # a 가 N//4 되면 종료
        if a == N//4:
            break
        # 아니면
        else:
            # 0이 아닌 곳에서
            for i in range(N // 4 - a, len(q), N // 4):
                hx_16 = ""
                # 16진수 짜른거를
                for j in range(N // 4):
                    hx_16 += q[i + j]
                # 10 진수로 중복없이 set에 add
                num_s.add(int(hx_16, 16))

        # 원형큐처럼 뒤에거 앞으로 보내기
        q[N//4 - 1 - a] = q[-1]
        # 뒤에거는 지우고
        q.pop()
        # N//4 까지 반복하기 위한 조건
        a += 1

    # 중복제거한 숫자들 리스트로
    num_l = list(num_s)
    # 내림차순
    num_l.sort(reverse=True)
    # K번째 숫자 출력
    print(f"#{tc} {num_l[K-1]}")