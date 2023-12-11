import sys
from collections import deque

N = int(sys.stdin.readline())
# enumerate는 인덱스와 값 튜플로 저장
q = deque(enumerate(map(int, input().split())))

# print(N)
# print(q)
answer = []
while q:
    idx, move = q.popleft()
    answer.append(idx + 1)

    # rotate(-1) 반시계 방향
    # rotate(1) 시계 방향
    if move > 0:
        q.rotate(-(move - 1))
    else:
        q.rotate(-move)

print(*answer)