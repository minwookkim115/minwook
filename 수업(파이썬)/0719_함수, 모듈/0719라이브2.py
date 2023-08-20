# import sys

# sys.stdin = pent('input.txt')

# T = int(input())

# K, N , M = map(int, input().split())

# zip
# names = ['Alice', 'Bob', 'Charlie']
# ages = [30, ,25, 35]
# cities = ['New York', 'London', 'Paris']

# for name, age, city in zip(names, ages, cities)


keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(my_dict) # {'a': 1, 'b': 2, 'c': 3}