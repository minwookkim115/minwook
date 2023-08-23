import sys

sys.stdin = open("16692_input.txt", "r")


# 중위순회
def inorder(t):
    global num
    # t가 숫자고
    if t:
        # t가 N보다 작을 때
        if t <= N:
            inorder(t * 2)  # L로
            # V에서 처리
            node[t] = num  # num 추가하고
            num += 1  # num에 + 1
            inorder(t * 2 + 1)  # R로
    return node


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # N + 1만큼의 노드 생성
    node = [0] * (N + 1)

    num = 1

    tree = inorder(1)
    print(f"#{tc} {tree[1]} {tree[N // 2]}")
