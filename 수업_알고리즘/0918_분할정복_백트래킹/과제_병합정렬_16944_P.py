import sys

sys.stdin = open("16944_input.txt")


# 병합함수
def merge(left, right):
    result = []  # 왼쪽과 오른쪽을 합친 결과
    global count  # 오른쪽을 먼저 다썼을 때 카운트

    # i => 왼쪽 리스트에서 원소를 꺼낼 위치
    # j => 오른쪽 리스트에서 원소를 꺼낼 위치
    i, j = 0, 0

    while True:
        # i와 j가 left right의 길이보다 작으면
        # left right 둘다 원소가 있다.
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:  # left의 i번째가 더 작으면
                result.append(left[i])  # left거 넣고
                i += 1  # left인덱스에 + 1
            else:  # right의 j번째가 더 작으면
                result.append(right[j])  # right거 넣고
                j += 1  # right 인덱스에 + 1
        # right는 비고 left만 남았을 때
        elif i < len(left):
            count += 1  # count + 1 해주고
            for k in range(i, len(left)):  # i번째부터 남은거
                result.append(left[k])  # 다 넣기
                i += 1  # while문 끝날 수 있도록 i에 + 1
        # left는 비고 right만 남았을 때
        elif j < len(right):
            for k in range(j, len(right)):  # j번째부터 남은거
                result.append(right[k])  # 다 넣기
                j += 1  # while문 끝날 수 있도록 j에 + 1
        # 다 넣었으면 break
        else:
            break

    return result


# lst : 정렬할 리스트
def mergeSort(lst):
    m = len(lst)

    # 종료 조건 (더이상 분할 못할때 까지)
    if m == 1:
        return lst

    # 분할
    mid = m // 2
    left, right = lst[:mid], lst[mid:]  # 얕은 복사

    # 정복
    left = mergeSort(left)  # 왼쪽 정렬
    right = mergeSort(right)  # 오른쪽 정렬

    # 병합
    return merge(left, right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))

    count = 0

    print(f"#{tc} {mergeSort(ai)[N // 2]} {count}")
