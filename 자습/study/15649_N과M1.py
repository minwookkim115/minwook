# 첫 째 자리 1 까지 돌고 재귀
# 둘 째 자리 2 까지 돌고 재귀
# 셋 째 자리 3 까지 돌고 재귀
# 넷 째 자리 4 까지 돌고 재귀
# 1234 출력하고 재귀 나오는데 => 4까지 돌았으니까 4 pop 하고 for 문 끝나고
# 3 pop 하고 for문에서 4 돌면서 124 로 가고 재귀 => 1243
# 3 pop 하고 for문 끝나고 4 pop 하고 for문 끝나고 => 2 pop 하면서 둘 째 자리 for 문이 3까지 돌고 재귀
# 반복
def answer(n, m):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(1, n + 1):
        if i not in arr:
            arr.append(i)
            answer(n, m)
            arr.pop()


N, M = list(map(int, input().split()))
arr = []

answer(N, M)
