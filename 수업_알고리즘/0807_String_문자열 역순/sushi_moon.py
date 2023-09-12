T = int(input())

for tc in range(1, T + 1):
    word = input()

    word_list = list(word)
    N = len(word_list)

    new_word_list = []

    answer = 0

    for i in range(N):
        new_word_list.append(word_list[N-1-i])

    new_word = "".join(new_word_list)

    if word == new_word:
        answer = 1

    print(f"#{tc} {answer}")