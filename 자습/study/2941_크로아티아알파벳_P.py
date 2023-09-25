string = input()

count = 0
i = 0

while i < len(string):
    if string[i] == "c":
        if i < len(string) - 1:
            if string[i + 1] == "=" or string[i + 1] == "-":
                count += 1
                i += 2
            else:
                count += 1
                i += 1
        else:
            count += 1
            i += 1

    elif string[i] == "d":
        if i < len(string) - 1:
            if string[i + 1] == "-":
                count += 1
                i += 2
            elif i < len(string) - 2:
                if string[i + 1] == "z" and string[i + 2] == "=":
                    count += 1
                    i += 3
                else:
                    count += 1
                    i += 1
            else:
                count += 1
                i += 1
        else:
            count += 1
            i += 1

    elif string[i] == "l":
        if i < len(string) - 1:
            if string[i + 1] == "j":
                count += 1
                i += 2
            else:
                count += 1
                i += 1
        else:
            count += 1
            i += 1

    elif string[i] == "n":
        if i < len(string) - 1:
            if string[i + 1] == "j":
                count += 1
                i += 2
            else:
                count += 1
                i += 1
        else:
            count += 1
            i += 1

    elif string[i] == "s":
        if i < len(string) - 1:
            if string[i + 1] == "=":
                count += 1
                i += 2
            else:
                count += 1
                i += 1
        else:
            count += 1
            i += 1

    elif string[i] == "z":
        if i < len(string) - 1:
            if string[i + 1] == "=":
                count += 1
                i += 2
            else:
                count += 1
                i += 1
        else:
            count += 1
            i += 1

    else:
        count += 1
        i += 1

print(count)
