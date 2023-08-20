T = int(input())

for tc in range(1, T + 1):
    P, A, B = map(int, input().split())

    l = 1
    r = P

    winner = ''

    A_search_count = 0
    B_search_count = 0

    while l <= r:
        c = int((l + r) / 2)
        if c == A:
            A_search_count += 1
            break
        elif c < A:
            l = c
            A_search_count += 1
        else:
            r = c
            A_search_count += 1

    l = 1
    r = P

    while l <= r:
        c = int((l + r) / 2)
        if c == B:
            B_search_count += 1
            break
        elif c < B:
            l = c
            B_search_count += 1
        else:
            r = c
            B_search_count += 1

    if A_search_count < B_search_count:
        winner = 'A'
    elif B_search_count < A_search_count:
        winner = 'B'
    else:
        winner = '0'

    print(f"#{tc} {winner}")
