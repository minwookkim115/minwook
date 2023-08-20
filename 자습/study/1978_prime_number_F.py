N = int(input())

num_list = list(map(int, input().split()))

prime_count = 0

for i in num_list:
    not_prime_count = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                not_prime_count += 1
        if not_prime_count == 0:
            prime_count += 1

print(prime_count)
