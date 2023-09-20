import sys

sys.stdin = open("17015_input.txt", "r")


# 일단 하나씩 집합 다 만들고
def make_set(x):
    p[x] = x
    rank[x] = 0


# 대장찾기
def find_set(x):
    # x가 대장이 아니면
    # 대장 찾으러 계속 올라감
    if x != p[x]:
        p[x] = find_set(p[x])

    return p[x]


# 합치기
def union(x, y):
    x = find_set(x)
    y = find_set(y)

    # 트리의 높이가 더 짧은애를 긴애한테 넣기
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


T = int(input())
for tc in range(1, T + 1):
    # N : 출석번호
    # M : M 쌍의 종이
    N, M = map(int, input().split())
    paper = list(map(int, input().split()))
    p = [0] * (N + 1)
    rank = [0] * (N + 1)

    # 일단 집합 다만들고
    for i in range(1, N + 1):
        make_set(i)

    # 합치고
    for i in range(0, M * 2, 2):
        union(paper[i], paper[i + 1])

    # 각각의 대장 찾기
    check = []
    for i in range(1, N + 1):
        if find_set(i) not in check:
            check.append(find_set(i))

    # 대장 몇명있는지
    count = 0
    for i in check:
        count += 1

    print(f"#{tc} {count}")
