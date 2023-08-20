import sys

sys.stdin = open("3143_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    t, p = input().split()

    pi = 0  # 비교 할 p의 시작점 (bana)
    ti = 0  # 비교 해야할 t의 시작점 (banana)

    count = 0  # 작성 횟수

    while ti < len(t):  # t_list 의 끝까지 검사

        if t[ti] == p[pi]:  # pi와 ti가 같으면, bana의b와 banana의b
            ti += 1  # 다음 검사
            pi += 1  # 다음 검사
            if pi == len(p):  # pi가 패턴 만큼 돌았으면 t안에 p가 있다는 뜻
                pi = 0  # pi를 다시 0으로 만들고 t가 len(t_list) 갈때 까지 검사
                count += 1  # t안에 p가 있는만큼 작성 + 1
            # ti가 len(t)로 가는 경우
            # 만약 banana에서 nan을 찾을 때 pi=0, ti=4 가 같으므로
            # pi=1, ti=5가 되고 또 같으므로
            # pi=2, ti=6이 되어야 하지만 불가능
            # 이 경우 nan을 찾지 못한다.
            # 그래서 ti == len(t)가 되었을 때 다시 검색하고 count에 + 1
            elif ti == len(t):
                ti = ti - pi + 1
                pi = 0
                count += 1
        else:  # 다르면
            ti = ti - pi + 1  # ti는 움직인 pi만큼 빼주고 다시 + 1
            pi = 0  # pi는 다시 0 으로
            count += 1  # 다르니까 그냥 + 1

    print(f"#{tc} {count}")