import sys

sys.stdin = open("17014_input.txt", "r")
from collections import deque

T = int(input())


def bfs(n):
    q = deque() # 큐에 저장
    # q = []

    v = [0] * 1000001 # 간곳 다시 안가도록 저장

    v[n] = 1 # 시작점 1로
    q.append(n) # q에 일단 append

    # 연산횟수
    cnt = 0

    # bfs
    while q:
        # bfs 단계 나누기
        size = len(q)

        # size 만큼 반복하면 한 단계 끝
        for _ in range(size):
            # a = q.pop(0)
            a = q.popleft() # q에 저장된 것 중에 앞에거 뽑아서
            if a == M: # 숫자 나왔으면
                return cnt # 리턴
            for i in (a + 1, a - 1, a * 2, a - 10): # bfs 자식노드 모두 탐색
                if 1 <= i <= 1000000 and v[i] == 0:
                    q.append(i) # 계산한적 없고 100만 아래면 append
                    v[i] = 1

        cnt += 1


for tc in range(1, T + 1):
    N, M = map(int, input().split())

    print(f"#{tc} {bfs(N)}")