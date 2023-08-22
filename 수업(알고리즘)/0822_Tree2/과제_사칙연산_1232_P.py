import sys

sys.stdin = open("1232_input.txt", "r")


# 후위순회
# L - R - V 순서로 보고
# L 과 R을 저장후 V로 연산 실행
def postorder(t):
    if t:
        # node[t]가 사칙연산이면
        if node[t] == "+" or node[t] == "-" or node[t] == "*" or node[t] == "/":
            # left에 왼쪽 자식 숫자
            left = postorder(cleft[t])
            # right에 오른쪽 자식 숫자
            right = postorder(cright[t])

            # 사칙연산 실행
            if node[t] == "+":
                node[t] = left + right
            if node[t] == "-":
                node[t] = left - right
            if node[t] == "*":
                node[t] = left * right
            if node[t] == "/":
                node[t] = left / right

            # 사칙연산을 실행한 node[t]를 리턴
            return node[t]
    # 함수가 한번 끝날 때 마다 node[t] return
    # 안해주면 left right에 저장 안되고
    # None값으로 떠서 계산 안됨
    return node[t]


T = 10
for tc in range(1, T + 1):
    N = int(input())

    # 왼쪽자식과 오른쪽자식 만들기
    cleft = [0] * (N + 1)
    cright = [0] * (N + 1)

    # 노드 만들기
    node = [0] * (N + 1)

    for i in range(N):
        # 노드 정보
        info = input().split()

        # 현재 노드 번호
        p = int(info[0])
        l = len(info)

        if l >= 3:  # 3 이상이면
            cleft[p] = int(info[2])  # 왼쪽 자식
            if l == 4:  # 4 면
                cright[p] = int(info[3])  # 오른쪽 자식

        # 노드정보에서 1번째 자리(노드에 들어갈 사칙연산 or 숫자)가
        # 사칙연산이면
        if info[1] == "+" or info[1] == "-" or info[1] == "*" or info[1] == "/":
            node[p] = info[1]  # 그냥 추가
        else:  # 숫자면
            # 연산은 실수로 한다고 했으므로 float로 추가
            node[p] = float(info[1])

    print(f"#{tc} {int(postorder(1))}")
