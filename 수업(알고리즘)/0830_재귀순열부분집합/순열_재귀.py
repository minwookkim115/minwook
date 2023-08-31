def f(i, N):
    global count
    if i == N:  # 순열 완성
        print(p, count)
        count = 0
        return
    else:  # p[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0:  # 아직 사용되기 전
                p[i] = card[j]
                used[j] = 1
                f(i + 1, N)
                count += 1
                used[j] = 0


card = list(map(int, input()))
used = [0] * 4  # 이미 사용한 카드인지 표시
p = [0] * 4
count = 0
f(0, 4)

"""
124783
"""
