import sys
sys.stdin = open("3499_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 카드 개수
    card = list(input().split()) # 카드에 써진 문자

    l_card = len(card) # 카드 길이
    cut = len(card) // 2 # 자를 부분

    # card에서 반 자른거
    cut_l = []
    # 짝수일 때는
    if l_card % 2 == 0:
        # cut부터 시작해서 cut_l에 append
        for i in range(cut, l_card):
            cut_l.append(card[i])
    # 홀수일 때는
    else:
        # cut+1 부터 시작해서 cut_l에 append
        for i in range(cut + 1, l_card):
            cut_l.append(card[i])

    # 자른만큼 card에서 제거
    # 짝수일 때
    if l_card % 2 == 0:
        # cut부터 pop
        for i in range(cut, l_card):
            card.pop()
    # 홀수일 때
    else:
        # cut+1 부터 pop
        for i in range(cut + 1, l_card):
            card.pop()

    # 합치기
    i = 0
    j = 0
    # j가 돌때 까지
    while j < len(card):
        # cut_l에 0 2 4... 인덱스에
        # card를 하나씩 삽입
        cut_l.insert(i, card[j])
        i += 2 # 넣을 곳 인덱스 2씩 증가
        j += 1 # 넣을 원소 인덱스는 1씩 증가

    print(f"#{tc}", *cut_l)