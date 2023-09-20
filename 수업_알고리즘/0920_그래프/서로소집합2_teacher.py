p = [0] * 7
rank = [0] * 7


# 1. 집합 초기화
def make_set(x):
    p[x] = x
    # 처음 트리의 깊이는 0
    rank[x] = 0


# 2. 대표를 찾는 연산
def find_set(x):
    # 경로 압축
    if x != p[x]:
        p[x] = find_set(p[x])

    return p[x]


def find_set2(x):
    while x != p[x]:
        x = p[x]

    return x


# 3. 두 집합을 합치는 연산
def union(x, y):
    # x집합의 대표와 y집합의 대표를 찾기
    x = find_set(x)
    y = find_set(y)

    # x집합과 y집합을 합칠 때 트리의 깊이가 더 큰쪽이 대표가 된다.
    # x집합의 깊이가 y집합의 깊이보다 크니까 대표를 x로
    if rank[x] > rank[y]:
        p[y] = x
    else:
        # 그게 아니면 일단 대표를 y로
        p[x] = y
        # 만약 두 집합의 깊이가 같은 경우 깊이 + 1 증가
        if rank[x] == rank[y]:
            rank[y] += 1


for i in range(1, 7):
    make_set(i)

union(1, 3)
union(2, 3)
union(5, 6)
union(1, 5)
print(p)
print(find_set(1))  # find_set을 해줘야 경로압축이 됨
print(p)
