"""
4
1 2 1 3 3 4 3 5
"""

N = 5
E = int(input())
tree = list(map(int, input().split()))

# 1. 인덱스 번호 => 부모노드의 번호
child_left = [0] * (N + 1)  # child_left[i] => i의 왼쪽자식 노드 번호
child_right = [0] * (N + 1)  # child_right[i] => i의 오른쪽자식 노드 번호

for i in range(E):
    parent = tree[i * 2]
    child = tree[i * 2 + 1]
    # 왼쪽 자식이 비어있으면 왼쪽부터 추가
    if child_left[parent] == 0:
        child_left[parent] = child
    else:
        child_right[parent] = child

# 2. 인덱스 번호 => 자식노드의 번호
parent = [0] * (N + 1)  # parent[i] => i번째 노드의 부모노드 번호
for i in range(E):
    p = tree[i * 2]
    c = tree[i * 2 + 1]
    parent[c] = p

print(child_left)
print(child_right)

print(parent)

# 조상노드 찾기
now = 5

while parent[now] != 0:
    print(parent[now])
    now = parent[now]
