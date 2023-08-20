T = int(input())

days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

for test_case in range(1, 1+T):

    calendar = str(input())

    year = calendar[0:4]
    month = calendar[4:6]
    day = calendar[6:8]

    if int(year) > 0:
        if 0 < int(month) <= 12 and int(day) <= days[int(month)]:
            print(f"#{test_case} {year}/{month}/{day}")

        else:
            print(f"#{test_case} -1")