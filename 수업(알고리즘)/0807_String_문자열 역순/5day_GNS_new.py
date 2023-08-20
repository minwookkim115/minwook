import sys

sys.stdin = open("GNS_test_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    M, N = map(str, input().split())

    num_list = list(map(str, input().split()))

    count = [0] * 10


