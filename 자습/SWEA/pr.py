import sys
sys.stdin = open("1926_input.txt", "r")

N = int(input())
num_l = []
for i in range(1, N + 1):
    num_l.append(str(i))

for i in range(len(num_l)):
    if num_l[i] == "3" or num_l[i] == "6" or num_l[i] == "9":
        num_l[i] = "-"

    if "3" in num_l[i] or "6" in num_l[i] or "9" in num_l[i]:
        if len(num_l[i]) == 2:
            if num_l[i][0] == "3" or num_l[i][0] == "6" or num_l[i][0] == "9":
                if num_l[i][1] == "3" or num_l[i][1] == "6" or num_l[i][1] == "9":
                    if len(num_l[i]) == 3:
                        if num_l[i][2] == "3" or num_l[i][2] == "6" or num_l[i][2] == "9":
                            num_l[i] = "---"
                        else:
                            num_l[i] = "--"
                    else:
                        num_l[i] = "--"
                else:
                    num_l[i] = "-"
            elif num_l[i][1] == "3" or num_l[i][1] == "6" or num_l[i][1] == "9":
                num_l[i] = "-"


print(*num_l)