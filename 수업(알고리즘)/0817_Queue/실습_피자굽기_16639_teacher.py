import sys
sys.stdin = open("16639_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    # N은 오븐크기, M은 피자 개수
    N, M = map(int, input().split())

    # 우리가 구워야할 피자들의 치즈 정보
    pizza_list = list(map(int, input().split()))

    # 다음에 꺼내올 피자 인덱스
    next_i = 0

    # 오븐을 큐로 만들어 보자
    oven = [0] * 1000
    ofront = orear = -1

    # 오븐의 크기만큼 피자 넣어주기
    for i in range(N):
        # 오븐에 피자 넣기
        orear += 1
        # 나중에 꺼낼때를 위해서 피자 번호도 같이 넣기
        oven[orear] = [i, pizza_list[i]]
        next_i += 1

    # 오븐에 남아있는 피자의 개수
    remain = N
    # 마지막에 꺼낸 피자의 번호
    last_idx = -1

    # 모든 피자의 치즈가 녹을때까지 반복
    while True:
        # 피자를 하나 꺼내서
        ofront += 1
        pizza_idx, pizza = oven[ofront]
        # 치즈를 녹이고 c // 2
        pizza //= 2
        # 남은 치즈의 양이 0이 아니다 ==> 오븐에 다시 넣기
        if pizza != 0:
            orear += 1
            oven[orear] = [pizza_idx, pizza]  # 피자번호, 피자치즈
        # 남은 치즈 양이 0이 되었다
        else:
            # 현재 오븐의 자리에 남은 피자하나 꺼내서 넣기
            if next_i < M:
                orear += 1
                oven[orear] = [next_i, pizza_list[next_i]]
                # 하나 꺼냈으니까
                next_i += 1
            # 넣을피자가 없다.
            else:
                remain -= 1
                # 오븐에 남은 피자도 없는 상황이 온다
                if remain == 0:
                    # 현재 피자의 번호가 답이 된다
                    last_idx = pizza_idx
                    # 답을 구하고
                    # 반복 종료
                    break

    print(f"#{tc} {last_idx + 1}")
