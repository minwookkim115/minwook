c = []
g = []
for _ in range(20):
    subject, num, p = map(str, input().split())

    if p == 'A+':
        c.append(float(num))
        g.append(4.5)
    elif p == 'A0':
        c.append(float(num))
        g.append(4.0)
    elif p == 'B+':
        c.append(float(num))
        g.append(3.5)
    elif p == 'B0':
        c.append(float(num))
        g.append(3.0)
    elif p == 'C+':
        c.append(float(num))
        g.append(2.5)
    elif p == 'C0':
        c.append(float(num))
        g.append(2.0)
    elif p == 'D+':
        c.append(float(num))
        g.append(1.5)
    elif p == 'D0':
        c.append(float(num))
        g.append(1.0)
    elif p == 'F':
        c.append(float(num))
        g.append(0.0)

s = 0
for i in range(len(c)):
    s += c[i] * g[i]

print(s/sum(c))