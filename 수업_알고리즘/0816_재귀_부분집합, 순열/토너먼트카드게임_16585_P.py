import sys

sys.stdin = open("16585_input.txt", "r")


def tournament(i, j):
    # 종료조건
    # 더이상 두부분으로 쪼갤수가 없을때 ==> i~j까지 사이에 있는 사람이 1명
    if i == j:
        # i번째 사람 이라고 return
        return i
    # 재귀호출
    else:
        # 왼쪽 부분
        left = tournament(i, (i + j) // 2)
        # 오른쪽 부분
        right = tournament((i + j) // 2 + 1, j)

        # 왼쪽과 오른쪽 중에서 승자를 골라서 return
        # cards[left] => 왼쪽 사람이 낸 패
        # cards[right] => 오른쪽 사람이 낸 패

        # 승자를 판별하는 코드??

        if cards[left] == 1:
            if cards[right] == 1 or cards[right] == 3:
                return left
            else:
                return right
        if cards[left] == 2:
            if cards[right] == 2 or cards[right] == 1:
                return left
            else:
                return right
        if cards[left] == 3:
            if cards[right] == 3 or cards[right] == 2:
                return left
            else:
                return right


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    cards = list(map(int, input().split()))

    print(f"#{tc}", tournament(0, N - 1) + 1)
