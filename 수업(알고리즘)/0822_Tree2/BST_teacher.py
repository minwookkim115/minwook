"""
7
9 4 9 12 4 3 4 6 12 15 15 13 15 17
"""

cleft = [0] * 20
cright = [0] * 20

E = int(input())
tree = list(map(int, input().split()))

for i in range(E):
    p, c = tree[i * 2], tree[i * 2 + 1]

    # 루트를 기준으로 루트보다 작으면 왼쪽 자식으로, 루트보다 크면 오른쪽 자식으로
    if p < c:
        cright[p] = c
    else:
        cleft[p] = c


def search(node, key):
    if key == node:
        print(f"find : {node} == {key}")
        return node
    elif key > node:
        print("right", node, cright[node])
        return search(cright[node], key)
    else:
        print("left", node, cleft[node])
        return search(cleft[node], key)


def search2(node, key):

    while node:
        if key == node:
            print(f"find : {node} == {key}")
            return node
        elif key > node:
            print("right", node, cright[node])
            node = cright[node]
        else:
            print("left", node, cleft[node])
            node = cleft[node]

    return None


print(search(9, 13))
print(search2(9, 13))