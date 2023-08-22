import sys

sys.stdin = open("16691_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())  # E = 간선의 개수 / N = 루트
    tree = list(map(int, input().split()))

    # 이진트리의 간선의 개수는 정점 - 1
    # 정점은 E + 1
    # 노드가 1부터 시작하니까
    # E + 2를 곱하기
    ch_l = [0] * (E + 2)
    ch_r = [0] * (E + 2)
    # 순회하면서 루트 아래에 몇개가 있는지 count
    count = 0

    # 간선 수만큼 돌면서
    for i in range(E):
        p = tree[i * 2]  # 부모노드
        c = tree[i * 2 + 1]  # 자식노드
        if ch_l[p] == 0:  # 부모노드의 인덱스가 비어 있으면
            ch_l[p] = c  # 왼쪽에 자식노드 추가
        else:
            ch_r[p] = c  # 부모노드가 안비어 있으면 오른쪽에 자식노드 추가

    # 전위순회
    def preorder(t):
        global count
        if t:  # 숫자가 있으면
            count += 1  # count에 + 1
            preorder(ch_l[t])  # 왼쪽 순회
            preorder(ch_r[t])  # 오른쪽 순회
        return count


    print(f"#{tc} {preorder(N)}")
