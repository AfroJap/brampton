# openBookTest1 -- Gursimran Shinger -- 7.12.17

def game1(FirstValue):
    sum = 0
    eund = 0
    while eund != dund:
        eund = int(input("Enter your guess for the random number"))
        sum = sum + 1
    return sum

def game2(SecondValue):
    sum = 0
    gund = 0
    while gund != fund:
        gund = int(input("Enter your guess for the random number"))
        sum = sum + 1
    return sum
beta = 0
while beta != 1:
    a = []
    bund = ""
    for i in range(0, 4):
        bund = input("Enter team name")
        a.append(bund)

    from random import randint
    aund = randint(0, 3)
    cund = randint(0, 3)
    while aund == cund:
        cund = randint(0, 3)

    print(" ")
    print("Team ", a[aund], " and Team ", a[cund], "have been selected to play")

    print("")
    print("Team ", a[aund], ":")
    dund = randint(0, 10)
    tries = 0
    tries = game1(dund)
    print("Team ", a[aund], " took ", dund, " tries")

    print("")
    print("Team ", a[aund], ":")
    fund = randint(0, 10)
    tries = 0
    tries = game2(fund)
    print("Team ", a[aund], " took ", fund, " tries")

    if dund > fund:
        print("Team ", a[aund], "wins")
    if fund > dund:
        print("Team ", a[cund], "wins")
    if dund == fund:
        print("It's a draw")

    print(" ")
    deta = input("Do you want to play a again, y or n?")
    if deta == "n":
        beta = 1
