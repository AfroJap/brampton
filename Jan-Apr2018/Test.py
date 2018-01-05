# January Assessment - Gursimran Shinger - 5.1.17

toppings = [["Cheese", "Ham", "Pepperoni", "Pineapple", "Mushroom", "Cherry Tomatoes", "Chicken", "Peppers", "Olives", "Jalepenos"],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]

print(1, toppings[0][0], toppings[1][0])
print(2, toppings[0][1], toppings[1][1])
print(3, toppings[0][2], toppings[1][2])
print(4, toppings[0][3], toppings[1][3])
print(5, toppings[0][4], toppings[1][4])
print(6, toppings[0][5], toppings[1][5])
print(7, toppings[0][6], toppings[1][6])
print(8, toppings[0][7], toppings[1][7])
print(9, toppings[0][8], toppings[1][8])
print(10, toppings[0][9], toppings[1][9])

HeldOrder = ["Order Number: ", 1, "  Base: ", "", "  Toppings Selected: ", 1, 1, 1, 1, 1]*20

y = 1
for i in range(0, 20):
    print()
    HeldOrder[1][i] = y
    y = y + 1
    bund = "y"
    while bund != "T" or "P":
        print("Please select if you want [T]hin or [P]an")
        bund = input()
    if bund == "T":
        HeldOrder[3][i] = "Thin"
    if bund == "P":
        HeldOrder[3][i] = "Pan"
    aund = 0
    for q in range(0, 5):
        while aund > 1 or aund < 10:
            print("Please enter the number you want for topping number ", q)
            aund = input()
            HeldOrder[6][i] = aund







