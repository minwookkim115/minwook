import sys

sys.stdin = open("4013_input.txt", "r")

T = int(input())

N = 0
S = 1


def rotate(o_g, o_d):  # o_g : 최초 자석 번호, o_d : 최초 방향
    g = o_g
    d = o_d
    l = g - 1
    r = g + 1

    rotate_lst = [(g, d)]  # g번 자석을 d 방향으로 회전할꺼다.

    # 왼쪽에 자석이 있으면 왼쪽 자석 회전할지 판단
    # g기준 왼쪽 자석 돌리기
    # g번 자석의 6번 날과 l번 자석의 2번 날 비교해서 다르면 왼쪽 자석 회전
    while l >= 0:
        if gears[g][6] != gears[l][2]:
            rotate_lst.append((l, -d))
        else:
            break

        g -= 1
        l -= 1
        d = -d

    g = o_g
    d = o_d
    # 오른쪽을 비교할때는 g번 자석의 2번 날과 r번 자석의 6번날 비교해서 다르면 회전
    while r < 4:
        if gears[g][2] != gears[r][6]:
            rotate_lst.append((r, -d))
        else:
            break
        d = -d
        g += 1
        r += 1

    # 회전할거 리스트에서 하나씩 꺼내서 회전
    for gi, di in rotate_lst:
        # gi : 회전할 자석 번호, di : 회전 방향
        if di == 1:  # 오른쪽
            gears[gi] = [gears[gi].pop()] + gears[gi]
        else:  # 왼쪽
            gears[gi] = gears[gi][1:] + [gears[gi].pop(0)]


for tc in range(1, T + 1):
    K = int(input())

    gears = [list(map(int, input().split())) for _ in range(4)]

    for i in range(K):
        g, d = map(int, input().split())  # g: 회전 시작 자석 번호, d: 회전 방향T
        g -= 1
        rotate(g, d)

    score = 0
    for i in range(4):
        if gears[i][0] == S:
            score += 2**i

    print(f"#{tc} {score}")
