T = int(input())

for tc in range(1, 1 + T):
    N = int(input())
    color_list = [list(map(int, input().split())) for _ in range(N)]

    red_colored_range = []
    blue_colored_range = []

    for i in color_list:
        if i[4] == 1:
            r_color_range = []
            r_color_range.extend([[i[0], i[1]], [i[2], i[3]]])

            color_range_r = r_color_range[1][0] - r_color_range[0][0]
            color_range_c = r_color_range[1][1] - r_color_range[0][1]

            for r in range(0, color_range_r + 1):
                for c in range(0, color_range_c + 1):
                    red_colored_range.extend([[r_color_range[0][0] + r, r_color_range[0][1] + c]])
        else:
            b_color_range = []
            b_color_range.extend([[i[0], i[1]], [i[2], i[3]]])

            color_range_r = b_color_range[1][0] - b_color_range[0][0]
            color_range_c = b_color_range[1][1] - b_color_range[0][1]

            for r in range(0, color_range_r + 1):
                for c in range(0, color_range_c + 1):
                    blue_colored_range.extend([[b_color_range[0][0] + r, b_color_range[0][1] + c]])

    purple_count = 0

    for i in red_colored_range:
        for j in blue_colored_range:
            if i == j:
                purple_count += 1

    print(f"#{tc} {purple_count}")