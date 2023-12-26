N, M = map(int, input().split())
nums = list(map(int, input().split()))

i = 0
sub = 0
while True:
    if i == M:
        break
    nums.sort()
    sub += nums[0] + nums[1]
    nums[0] = sub
    nums[1] = sub
    sub = 0
    i += 1

print(sum(nums))