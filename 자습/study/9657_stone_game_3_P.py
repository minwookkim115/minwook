N = int(input())

dp_cy = [2]

name = "SK"
for i in range(1, N + 1):
    if i < 5:
        if i == 2:
            name = "CY"
        else:
            name = "SK"

    if i >= 5:
        if i - 1 in dp_cy or i - 3 in dp_cy or i - 4 in dp_cy:
            name = "SK"
        else:
            name = "CY"
            dp_cy.append(i)
print(name)