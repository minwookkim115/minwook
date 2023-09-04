import sys
sys.stdin = open("1244_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    num, c = map(int, input().split())