import sys
sys.stdin = open("7087_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 문자 개수
    str_l = [input() for _ in range(N)] # 입력받을 문자

    str_l.sort() # 정렬

    # 앞 글자만 따고
    # 중복 없애주는 set
    head_l = set()
    for i in range(len(str_l)):
        # 아스키코드를 이용해서 숫자로 삽입
        head_l.add(ord(str_l[i][0]))

    # 다시 리스트로 만들어 주고
    num_l = list(head_l)

    # count 1로 초기화
    count = 1
    # 리스트 첫번째가 A(65)일때
    if num_l[0] == 65:
        # 다음 숫자(알파벳)가
        # 바로 이어지는 숫자(알파벳)면
        # + 1
        for i in range(len(num_l) - 1):
            if num_l[i] + 1 == num_l[i + 1]:
                count += 1
            # 아니면 반복문 종료
            else:
                break
    # 65가 아니면 count 0
    else:
        count = 0

    print(f"#{tc} {count}")