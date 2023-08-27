import sys

sys.stdin = open("4047_input.txt", "r")


# 카드 분별 함수
def cards(s, d, h, c):
    # 카드 정보가 들어있는 리스트 탐색하면서
    for i in range(len(card_l)):
        # 같은게 있으면
        for j in range(i + 1, len(card_l)):
            if card_l[i] == card_l[j]:
                # 에러 출력
                return "ERROR"
        # S, D, H, C 일때 하나씩 줄이기
        if card_l[i][0] == "S":
            s -= 1
        elif card_l[i][0] == "D":
            d -= 1
        elif card_l[i][0] == "H":
            h -= 1
        elif card_l[i][0] == "C":
            c -= 1
    # 같은거 없으면
    # S, D, H, C 리턴
    return s, d, h, c


T = int(input())
for tc in range(1, T + 1):
    card = input() # 일단 문자열로 받기

    # 모양 별로 13개의 카드
    S = D = H = C = 13

    # 카드 판별을 위해
    # 3개씩 잘라서 car_l에
    card_l = []

    # 3칸씩 뛰어서 돌면서
    for i in range(0, len(card), 3):
        # 카드 정보에
        card_info = ""
        # 3개씩 넣고
        for j in range(0, 3):
            card_info += card[i + j]
        # 리스트에 append
        card_l.append(card_info)

    answer = cards(S, D, H, C)

    # 에러는 그냥 출력
    if answer == "ERROR":
        print(f"#{tc} {answer}")
    # 에러아니면 언패킹해서 출력
    else:
        print(f"#{tc}", *answer)
