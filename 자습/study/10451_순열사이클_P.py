def find_answer(s):
    visited[s] = 1
    next = numbers[s]
    if visited[next] == 0:
        find_answer(next)
    return


T = int(input())
for _ in range(T):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [0] * (N + 1)
    answer = 0

    for i in range(1, N + 1):
        if visited[i] == 0:
            find_answer(i)
            answer += 1

    print(answer)