import sys

sys.stdin = open("16639_input.txt", "r")


def enqueue(item):


def dequeue():


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    q = [0] * N

    for i in range(N):
        q[i] = cheese[i]
