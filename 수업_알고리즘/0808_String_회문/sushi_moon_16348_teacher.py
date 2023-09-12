import sys
sys.stdin = open("16348_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    # 2차원 배열의 크기 N, 회문의 길이 M
    N, M = map(int, input().split())

    # 글자모음 ( 2차원 배열로 만들기 )
    text = [list(input()) for _ in range(N)]

    # 우리가 찾는 회문
    answer = ""

    # 행 우선 순회
    for i in range(N):  # i는 행번호
        for j in range(N - M + 1):  # j는 열번호
            # (i, j) 위치에 있는 글자부터 회문을 만들기 시작
            # 회문의 길이가 m 이니까 (i, j) ~ (i, j+,)까지의 글자를 모아서
            # 문자열로 만들면 완성 => 이 문자열이 회문인지 아닌지 검사
            # j의 범위 주의!! (인덱스 범위 벗어나지 않도록)
            # (i, j) 위치에서 문자열 만들기 시작
            word_row = ""
            # 글자 M 개 모아서 문자열 만들기
            for k in range(M):
                word_row += text[i][j + k]

            # word_row 가 회문인지 아닌지 판별(인덱스 연산)
            # word_row 가 회문이다 ==> answer = word_row

    # 열 우선 순회
    for i in range(N - M + 1):
        for j in range(N):
            word_col = ""
            for k in range(M):
                word_col += text[i + k][j]

