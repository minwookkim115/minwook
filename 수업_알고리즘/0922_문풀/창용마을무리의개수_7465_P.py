import sys

sys.stdin = open("7465_input.txt", "r")

T = int(input())


def find_set(x):
    # 집합이 만들어 졌을 때
    # 자기자신이 대장 아니면
    # 찾으러 올라가기
    if x != people[x]:
        people[x] = find_set(people[x])

    return people[x]


# 합치는 함수
def union(x, y):
    people[find_set(y)] = find_set(x)


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    know = [list(map(int, input().split())) for _ in range(M)]

    # 사람들 list
    # 일단 하나씩 집합 만들기
    people = []
    for i in range(N + 1):
        people.append(i)

    # 합치고
    for i in know:
        union(i[0], i[1])

    # 대장 찾기
    check = []
    for i in range(1, N + 1):
        if find_set(i) not in check:
            check.append(find_set(i))

    print(f"#{tc} {len(check)}")
