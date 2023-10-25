import sys

number = list(map(int, sys.stdin.readline().strip()))

number.sort(reverse=True)

print(*number, sep='')