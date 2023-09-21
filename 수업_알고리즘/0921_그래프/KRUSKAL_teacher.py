def find_set(x):
    while x != p[x]:
        x = p[x]

    return x


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x < y:
        p[y] = x
    else:
        p[x] = y


V, E = map(int, input().split())
edge = []

"""
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
"""

for _ in range(E):
    s, e, w = map(int, input().split())
    edge.append((w, s, e))  # 리스트 넣을 때 가중치를 맨 앞으로

edge.sort()  # 맨 앞 원소(가중치) 기준으로 오름차순 정렬

p = [i for i in range(V)]  # 서로소 집합을 만드는데 사용할 트리

cnt = 0
total = 0

# 정렬된 리스트를 순회하면서 가중치가 작은 간선의 정보부터 확인
for w, s, e in edge:
    # s 정점이 속한 집합의 대표와 e 정점이 속한 집합의 대표가 달라야 한다.
    # 대표가 같으면 같은 집합에 속해 있다는 의미 => 싸이클이 생김
    if find_set(s) != find_set(e):
        cnt += 1
        union(s, e)
        total += w
        if cnt == V:
            break
        # MST 구성이 끝나면 종료

print(total)