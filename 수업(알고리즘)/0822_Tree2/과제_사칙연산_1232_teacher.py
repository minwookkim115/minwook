import sys

sys.stdin = open("1232_input.txt", "r")


def postorder(t):
    # t번 노드가 숫자다 => 그냥 그 값을 되돌려 주기만 하면 된다.
    if node[t].isdigit():
        return float(node[t])
    # t번 노드가 숫자가 아니면
    else:
        # L => 왼쪽 자식 방문해서 결과값 가져오기
        left = postorder(cleft[t])
        # R => 오른쪽 자식 방문해서 결과값 가져오기
        right = postorder(cright[t])
        # V => 현재 노드 방문 처리 => 계산
        if node[t] == "+":
            node[t] = left + right
        elif node[t] == "-":
            node[t] = left - right
        elif node[t] == "*":
            node[t] = left * right
        elif node[t] == "/":
            node[t] = left / right

        return node[t]


T = 10
for tc in range(1, T + 1):
    N = int(input())

    # 왼쪽 자식
    cleft = [0] * (N + 1)
    # 오른쪽 자식
    cright = [0] * (N + 1)

    # i번 노드에 어떤 값(연산자 또는 피연산자)가 들어있는지
    # 변환표
    node = [0] * (N + 1)

    for i in range(N):
        info = input().split()

        # 노드의 번호 (0번째 값)
        t = int(info[0])

        # 연산자 or 피연산자 (1번째 값)
        if info[1].isdigit():
            # 1번째 값이 숫자면
            node[t] = info[1]
        else:
            # 1번째 값이 연산자면
            # 양 옆에 자식 노드가 존재 한다.
            node[t] = info[1]
            cleft[t] = int(info[2])
            cright[t] = int(info[3])

    print(f"#{tc} {int(postorder(1))}")