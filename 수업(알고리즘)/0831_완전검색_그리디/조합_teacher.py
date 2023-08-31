lst = [1, 2, 3, 4, 5]
N = 5
R = 3


# 내가 idx 번째 숫자를 고를지 안고를지
# r번 골랐다면 종료(또는 n번 고를지 안고를지 선택을 다 완료 했다면)
def comb(idx, r, selected):
    # 고를지 안고를지 n개의 원소에 대해 다 판단을 했다면면
    if idx == N:
        if r == R:
            # R개 골랐을때만
            print([lst[i] for i in selected])
        return

    # 내가 idx 번째에 있는 숫자를 골랐다.
    selected.append(idx)
    comb(idx + 1, r + 1, selected)
    # 내가 idx 번째에 있는 숫자는 안골랐다.
    selected.pop()
    comb(idx + 1, r, selected)


comb(0, 0, [])
