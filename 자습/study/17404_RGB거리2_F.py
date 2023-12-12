N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

answer = 10000000
min_v = 10000000

for i in range(3): # 첫번 째 집 RGB로 칠하면서
    check = [[min_v, min_v, min_v] for _ in range(N)]
    check[0][i] = house[0][i]
    for j in range(1, N): # 두번 째 집부터 최솟값 더해 가기
        check[j][0] = house[j][0] + min(check[j - 1][1], check[j - 1][2])
        check[j][1] = house[j][1] + min(check[j - 1][0], check[j - 1][2])
        check[j][2] = house[j][2] + min(check[j - 1][0], check[j - 1][1])
    for m in range(3):
        if i != m: # 첫번째 집이랑 마지막집이 다르면
            answer = min(answer, check[-1][m])

print(answer)