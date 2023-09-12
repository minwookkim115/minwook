numbers = ['1', '2', '3', '4', '5']

max1 = max(numbers)
max2 = 0
for i in range(len(numbers)):
    if numbers[i] == max(numbers):
        numbers.pop(i)
        max2 = max(numbers)
        numbers.insert(i, max1)
print(max1, max2)
print(numbers)

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
