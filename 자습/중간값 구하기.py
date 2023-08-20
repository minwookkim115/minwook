N = int(input())

num_list = list(map(int, input().split()))

middle = N // 2

num_list.sort()

print(num_list[middle])