T = 10
for tc in range(1, T + 1):
    N = int(input())
    box_heights = list(map(int, input().split()))

    for i in range(N):
        high_point = 0
        low_point = 101
        for j in box_heights:
            if high_point < j:
                high_point = j
            if low_point > j:
                low_point = j

        box_heights[box_heights.index(high_point)] -= 1
        box_heights[box_heights.index(low_point)] += 1

    box_high_point = 0
    box_low_point = 101
    for i in box_heights:
        if box_high_point < i:
            box_high_point = i
        if box_low_point > i:
            box_low_point = i

    print(f"#{tc} {box_high_point - box_low_point}")
