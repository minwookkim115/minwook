N = int(input())
answer = 0
for _ in range(N):
    string = input()
    count = 0

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            new = string[i + 1:]
            if new.count(string[i]) > 0:
                count += 1

    if count == 0:
        answer += 1

print(answer)