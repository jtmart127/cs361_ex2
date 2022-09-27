import re


def printIndex(numberWanted):
    f = open("out.txt", "r")
    found = False
    wantedAmountOfSpaces = 0
    amountOfSpaces = 0
    count = 0

    for x in f:
        if not found:
            if (re.search("ld a0,\d+\(s\d+\)", x) is not None):
                count += 1
                if (count == numberWanted):
                    print(x, end="")
                    for i, c in enumerate(x):
                        if c.isdigit():
                            wantedAmountOfSpaces = i
                            break
                    wantedAmountOfSpaces -=2
                    found = True
        else: 
            for i, c in enumerate(x):
                    if c.isdigit():
                        amountOfSpaces = i
                        break
            if (amountOfSpaces == wantedAmountOfSpaces):
                print(x, end="")
                wantedAmountOfSpaces -= 2

for i in range(1, 61):
    print(i)
    printIndex(i)
    print("\n")
