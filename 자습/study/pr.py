T = int(input())
for tc in range(T):
    N = int(input())

    answer = 0

    answer_l = []

    count = 0

    for i in range(1, N+1):
        if i == 1:
            answer = 1
            answer_l.append(1)
        if i == 2:
            answer = 2
            answer_l.append(2)
        if i == 3:
            answer = 4
            answer_l.append(4)
        if i >= 4:
            count = sum(answer_l)
            answer = count
            answer_l.append(count)
            answer_l.pop(0)

    print(answer)

"""
10
1
2
3
4
5
6
7
8
9
10

"""