'''
V
부모 자식
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''


def preorder(n):
    if n:  # 자식이 존재하는 정점이면
        print(n)  # visit(n)
        preorder(ch1[n])  # 왼쪽 서브트리로 이동
        preorder(ch2[n])  # 오른쪽 서브트리로 이동


V = int(input())  # 정점수 = 마지막 정점 번호
E = V - 1  # tree의 간선 수 = 정점 수 - 1

arr = list(map(int, input().split()))

# 부모를 인덱스로 자식을 저장
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)
# 자식을 인덱스로 부모를 저장
par = [0] * (V + 1)

for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]
    if ch1[p] == 0:  # 자식1이 아직 없으면
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p  # 자식을 인덱스로 부모를 저장

print(ch1)  # 왼쪽 자식
print(ch2)  # 오른쪽 자식
print(par)  # 자식을 인덱스번호로

# 실제 루트 찾기
root = 1
while par[root] != 0:
    root += 1

preorder(root)
