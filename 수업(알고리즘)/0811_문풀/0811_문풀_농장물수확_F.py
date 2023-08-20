import sys
sys.stdin = open("농작물 수확_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    print(farm)

