a, b, c, d, e, f = map(int, input().split())

num_l = []

for i in range(-999, 1000):
    num_l.append(i)

answer_x = 0
answer_y = 0


def find(num_l):
    global answer_x
    global answer_y

    for x in num_l:
        for y in num_l:
            if c == a * x + b * y and f == d * x + e * y:
                answer_x = x
                answer_y = y
                return


find(num_l)
print(answer_x, answer_y)
