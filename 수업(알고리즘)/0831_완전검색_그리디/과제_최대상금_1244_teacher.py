import sys

sys.stdin = open("1244_input.txt", "r")


def swap(cnt):
    global answer
    val = int("".join(S))  # 문자열 배열 숫자로 만들기
    if (cnt, val) in visited:  # cnt번 바꾸기 진행할건데 이전에 만든적이있는 숫자면 진행x
        return

    # 전에 만든적 없는 숫자면 만든적 있다고 체크한뒤 진행
    visited.add((cnt, val))

    # 종료 조건 : 교환 횟수를 다 소모 했다면
    # 바꾼 결과물을 숫자로 바꿔서 최대상금 계산
    if cnt == N:
        answer = max(answer, val)
        return

    # 자리를 바꿀 위치 2개를 교환 한번 할때마다 새로 지정
    # 이 문제에서는 동일한 위치에서 중복 교환을 허용
    # 바꿀 위치중에 앞쪽: i
    # 바꿀 위치중에 뒤쪽: j
    for i in range(len(S) - 1):
        for j in range(i + 1, len(S)):
            S[i], S[j] = S[j], S[i]
            swap(cnt + 1)
            # 바꿨던거 원상 복구 시키고 새로운 i, j 지정
            S[i], S[j] = S[j], S[i]


T = int(input())
for tc in range(1, T + 1):
    S, N = input().split()
    S = list(S)
    N = int(N)

    visited = set()  # (k, num) : 자리를 k번 교환했을때 num을 만든적이 있다.
    answer = 0
    swap(0)

    print(f"#{tc} {answer}")
