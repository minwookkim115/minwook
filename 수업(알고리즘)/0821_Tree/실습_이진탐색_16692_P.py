import sys

sys.stdin = open("16692_input.txt", "r")


# 중위순회
def inorder(t):
    global num  # num은 1부터 시작
    if t:  # t가 숫자일 때
        inorder(cleft[t])  # L로
        # V에서 실행
        node[t] = num  # 노드의 t 번째에 num 삽입
        num += 1  # num + 1
        inorder(cright[t])  # R로
    return node


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # N + 1만큼의 노드 생성
    node = [0] * (N + 1)

    # 왼쪽 자식
    cleft = [0] * (N + 1)
    # 오른쪽 자식
    cright = [0] * (N + 1)

    # root인 1번 노드에는 왼쪽 자식에 2번 오른쪽 자식에 3번 연결
    # 2번 노드에는 왼쪽 자식에 4번 오른쪽 자식에 5번 연결
    i = 2
    j = 1
    # i가 N까지
    while i < N + 1:
        # 왼쪽 자식에 2, 4, 6, 순서로 N까지 삽입
        cleft[j] = i
        if i == N:  # N이 되면
            break  # break
        # 오른쪽 자식에는 3, 5, 7 순서로 N까지 삽입
        cright[j] = i + 1
        i += 2
        j += 1

    num = 1
    tree = inorder(1)
    answer1 = tree[1]  # node root에 들어간 num
    answer2 = tree[N // 2]  # node에 N//2에 들어간 num

    print(f"#{tc} {answer1} {answer2}")
