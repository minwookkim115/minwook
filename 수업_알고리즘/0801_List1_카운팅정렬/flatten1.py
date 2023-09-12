def maxx(list1):
    max = 0
    for i in list1:
        if max < i:
            max = i
    return max

def minn(list1):
    min = 101
    for i in list1:
        if min > i:
            min = i
    return min

for t in range(1, 11):
    tr = int(input())
    box = list(map(int, input().split()))

    for j in range(tr):
        max = maxx(box)
        min = minn(box)
        # print(f"before max = {max} min = {min}")
        box[box.index(max)] -= 1
        box[box.index(min)] += 1

        print(max, min)

        # print(f"after max = {max} min = {min}")

    #     if max - min <= 1:
    #         break
    #
    # result = max - min
    # print(f"#{t} {result}")