import sys
sys.stdin = open("5356_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):

    # 공백으로된 리스트를 길이 15에 5줄 생성
    string = [[""] * 15 for _ in range(5)]

    # 5줄 돌면서
    for i in range(5):
        # a로 input 받고
        a = input()
        # a를 돌면서
        for j in range(len(a)):
            # string에
            # i => 1 ~ 5 번째줄에
            # j 번째에다가 a[j] 넣기
            string[i][j] = a[j]

    # 세로 모음
    answer = ""
    # 길이(열) 15개 돌면서
    for c in range(15):
        # 줄(행) 5개 돌면서
        for r in range(5):
            # answer에다가 세로 모음
            answer += string[r][c]

    print(f"#{tc} {answer}")