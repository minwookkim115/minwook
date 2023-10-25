import sys
import heapq
N = int(input())

heap = []
for _ in range(N):
    num = int(sys.stdin.readline())

    heapq.heappush(heap, num)

heap.sort()

for i in heap:
    print(i)