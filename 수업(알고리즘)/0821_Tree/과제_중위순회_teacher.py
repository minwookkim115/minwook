import sys

sys.stdin = open("과제_input.txt", "r")

T = 10


def inorder(t):
    global result
    if t:
        inorder(cleft[t])
        # 방문 처리
        result += node[t]  # t번 노드에 해당하는 알파벳 붙이기
        inorder(cright[t])


for tc in range(1, T + 1):
    N = int(input())  # 정점의 개수

    cleft = [0] * (N + 1)
    cright = [0] * (N + 1)

    # 노드 번호 <=> 알파벳 변환 표 배열
    node = [0] * (N + 1)

    # 정점 정보를 토대로 트리 만들기
    for i in range(N):
        # 노드의 정보를 읽어오기
        # 쪼갠 다음에 글자의 개수를 세본다.
        info = input().split()
        # 0 : 노드의 번호
        # 1 : 알파벳
        # 2 : 왼쪽 자식 노드 번호
        # 3 : 오른쪽 자식 노드 번호
        p = int(info[0])  # 현재 노드 번호
        l = len(info)

        # 길이가 3 이상이면 자식 처리
        if l >= 3:
            cleft[p] = int(info[2])
            if l == 4:
                cright[p] = int(info[3])

        # 노드번호 p에는 알파벳이 저장되어 있다.
        # 변환표 작성
        node[p] = info[1]

        print(info)

    # 중위순회 하면서 문자열 출력
    result = ""
    inorder(1)
    print(f"#{tc} {result}")
