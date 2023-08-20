import sys
sys.stdin = open("과제_input.txt", "r")

T = 10

for tc in range(1, T + 1):
    N = int(input())
    str_board = [list(map(str, input())) for _ in range(8)] # 8*8의 글자 판

    count = 0 # 회문 개수
    for i in range(8): # 모든 행을 순회 하면서
        for j in range(8 - N + 1): # 열은 8-N+1 까지만 순회

            word_row = "" # str_board 를 순회 하면서 얻는 문자
            for k in range(N): # 문자열의 길이 N만큼
                # 모든 행을 순회하면서
                # 8-N+1까지 순회하는 열에
                # 문자열의 길이 N만큼 더하면서 word_row에 입력
                word_row += str_board[i][j + k]

            for l in range(N//2): # 회문은 앞뒤가 같기 때문에 N//2만큼 순회
                if word_row[l] != word_row[N-1-l]: # 앞 글자와 뒷 글자가 다르면
                    break # 그냥 끝내고
            else: # 앞 글자와 뒷 글자가 같은걸 발견하면
                count += 1 # count

    for i in range(8 - N + 1): # 행을 8-N-1 만큼 순회하면서
        for j in range(8): # 열은 모두 순회

            word_col = ""
            for k in range(N):
                # 열은 모두 순회 하면서
                # 8-N+1까지 순회하는 행에
                # 문자열의 길이 N만큼 더하면서 wor_col에 입력
                word_col += str_board[i + k][j]
            for l in range(N//2):
                if word_col[l] != word_col[N-1-l]:
                    break
            else:
                count += 1

    print(f"#{tc} {count}")