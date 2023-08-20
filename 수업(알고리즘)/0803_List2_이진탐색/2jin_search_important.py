def binarySearch(a, N, key):
    start = 0
    end = N - 1

    while start <= end:  # 탐색구간이 존재하면 or 원소가 한개 이상이면
        middle = (start + end) // 2
        if a[middle] == key:  # 검색 성공
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False
