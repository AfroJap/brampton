nullPointer = -1

class Order:
    def __init__(self):
        self.number = 0
        self.base = ""
        self.topping = []


class Node:
    def __init__(self):
        self.dataItem = ""
        self.NodeID = nullPointer

def SelectBase():
    while bund != "T" or "P":
       print("Please select if you want [T]hin or [P]an")
       bund = input()
    if bund == "T"



toppings = [["Cheese", "Ham", "Pepperoni", "Pineapple", "Mushroom", "Cherry Tomatoes", "Chicken", "Peppers", "Olives", "Jalepenos"],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]

for i in range(0, 10):
    print(i+1, toppings[0][i], toppings[1][i])


a = [Node(), Node(), Node(), Node(), Node(), Node(), Node(), Node(), Node(), Node()]
for i in range(0,6):
    a.append(Node())
    a[i].nodeID = i+1

    while bund != "T" or "P":
       print("Please select if you want [T]hin or [P]an")
       bund = input()
    a[counter] = bund
    while bund > 10 & bund < 1:
        print("Please select what topping you want[1-10]")
        bund = input()
    a[counter] = bundtho
    while bund != 0:
        while bund > 10 & bund < 0:
            print("Please select what topping you want[1-10], or enter you want no more toppings[0]")
            bund = input()
        a[counter] = bund
        q = toppings[1][bund]
        toppings[1][bund] = q - 1









