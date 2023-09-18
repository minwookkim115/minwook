import sys
sys.stdin = open("16944_input.txt")

# 병합함수
def merge(left, right):
    result = []  # 왼쪽과 오른쪽을 합친 결과
    global count

    i, j = 0, 0
    # i => 왼쪽 리스트에서 원소를 꺼낼 위치
    # j => 오른쪽 리스트에서 원소를 꺼낼 위치
    while True:
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif i < len(left):
            count += 1
            for k in range(len(left)):
                result.append(left[k])
                i += 1
        elif j < len(right):
            for k in range(len(right)):
                result.append(right[k])
                j += 1
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

    print(f"#{tc} {mergeSort(ai)} {count}")