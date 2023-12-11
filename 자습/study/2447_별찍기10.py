def make_star(n):
    if n == 1:
        return ['*']

    made_star = make_star(n // 3)
    stars = []

    for star in made_star:
        stars.append(star * 3)
    for star in made_star:
        stars.append(star + ' ' * (n // 3) + star)
    for star in made_star:
        stars.append(star * 3)

    return stars


N = int(input())
print('\n'.join(make_star(N)))
