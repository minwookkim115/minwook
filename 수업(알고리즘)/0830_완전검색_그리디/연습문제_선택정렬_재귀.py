# selection_sort(i): i번째 자리에 놓을 리스트에서 i번째로 작은 원소 찾기
# 리스트의 길이가 5라면??
# selection_sort(0): 0번 인덱스에 제일 작은 원소 놓기
# selection_sort(1): 1번 인덱스에 그 다음으로 작은 원소 놓기
# selection_sort(2): 2번 인덱스에 그 다음으로 작은 원소 놓기
# selection_sort(3): ...
# selection_sort(4): ...
# selection_sort(5) ==> 5번 인덱스는 범위를 벗어나니까 종료
# 종료조건 // 재귀호출


def selection_sort(i, lst):
    # 종료 조건
    if i == N:
        return
    # i번 인덱스에서 해야 할 일:
    # 제일 작은 값 찾아서 i번 인덱스에 놓기(자리교환)

    min_i = i  # 제일 작은값의 인덱스 찾기
    for j in range(i + 1, N):
        if lst[min_i] > lst[j]:
            min_i = j  # 제일작은 값의 인덱스 넣고
    lst[i], lst[min_i] = lst[min_i], lst[i]  # 제일 작은값이랑 앞이랑 바꾸기
    # 재귀 호출 (i+1)번 인덱스에 놓을 작은 원소 찾으러
    selection_sort(i + 1, lst)


arr = [3, 2, 4, 5, 1]
N = len(arr)
# 재귀호출 시작 : 0번째 자리에 놓을 제일 작은 원소 찾기
selection_sort(0, arr)

print(arr)
