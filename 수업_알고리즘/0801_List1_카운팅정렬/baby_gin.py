num_list = list(map(int, input()))

num_list_len = len(num_list)
check_list = [0] * 10

triplet = 0
run = 0

for i in range(num_list_len):
    check_list[num_list[i]] += 1

# for i in range(len(check_list)):
#     if check_list[i] >= 3:
#         check_list[i] -= 3
#         triplet += 1
#     if check_list[i] >= 1 and check_list[i + 1] >= 1 and check_list[i + 2] >= 1:
#         check_list[i] -= 1
#         check_list[i + 1] -= 1
#         check_list[i + 2] -= 1
#         run += 1
# ▲ 이렇게 하면 232311 일때 run 을 한번만 빼와서 안됨
# so while 을 써보자

i = 0
while i < 10:
    if check_list[i] >= 3:
        check_list[i] -= 3
        triplet += 1
        continue
    if check_list[i] >= 1 and check_list[i + 1] >= 1 and check_list[i + 1] >= 1:
        check_list[i] -= 1
        check_list[i + 1] -= 1
        check_list[i + 2] -= 1
        run += 1
        continue
    i += 1


if triplet + run == 2:
    print("baby gin")
else:
    print("lose")