import sys

sys.stdin = open("16720_input.txt", "r")


# L보고 R보고 V에서 계산해야 하니까
# 후위순회
def postorder(t):
    # N 보다 작을 때
    if t <= N:
        # 노드가 0이 아니면
        # 리프노드까지 가면
        if node[t] != 0:
            # 리프노드를 리턴
            return node[t]
        # 안가면
        else:
            left = postorder(t * 2)  # 왼쪽자식에서 리턴된 숫자
            right = postorder(t * 2 + 1)  # 오른쪽 자식에서 리턴된 숫자
            node[t] = left + right  # 두개 더해서 node[t]에
            if t == 1:  # 루트에 도착하면
                return node  # node를 리턴
            else:  # 루트 아니면
                return node[t]  # node[t]를 리턴하고 계속
    # N 보다 크면
    # ex) N이 10 일때
    # 부모노드 5에
    # 자식노드 10은 있지만 11은 없음
    else:
        return 0  # 없으니까 0 리턴


T = int(input())
for tc in range(1, T + 1):
    # N : 노드 개수
    # M : 리프의 개수
    # L : 출력할 노드 번호
    N, M, L = map(int, input().split())

    # 노드 만들고
    node = [0] * (N + 1)

    # 리프 개수 만큼 돌면서
    for _ in range(M):
        a, b = map(int, input().split())
        # 리프의 노드에 숫자 삽입
        node[a] = b

    tree = postorder(1)
    print(f"#{tc} {tree[L]}")
