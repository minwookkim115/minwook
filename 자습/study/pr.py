# import sys
# sys.stdin = open('input.txt', 'r')

A, B, V = map(int, input().split())

height = 0
count = 1
while True:
    height += A
    if height >= V:
        break
    else:
        height -= B
        count += 1

print(count)