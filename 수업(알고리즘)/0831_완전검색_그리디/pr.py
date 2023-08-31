numbers = ['1', '2', '3', '4', '5']

# n = len(numbers)
#
# def perm(i, selected):
#
#     # 종료 조건
#     if i == n:
#         print(selected)
#         return
#
#     for j in range(n):
#         if numbers[j] not in selected:
#             selected[i] = numbers[j]
#             perm(i + 1, selected)
#             selected[i] = 0
#
# perm(0, [0] * 5)
