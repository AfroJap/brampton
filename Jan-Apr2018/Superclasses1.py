#declare all characteristics

class toy:
    def __init__(self):
        self.name = "abc"
        self.ID = 30
        self.price = "£00.00"
        self.minAge = "7"

    def showname(self):
        name1 = self.type()
        print(name1)
    def showID(self):
        ID1 = self.type()
        print(ID1)
    def showPrice(self):
        price1 = self.type()
        print(price1)
    def showMinAge(self):
        minAge1 = self.type()
        print(minAge1)

class vehicle(toy):
    def __init__(self):
        self.type = "abc"
        self.height = 30
        self.length = 01
        self.weight = "1kg"

    def showType(self):
        type1 = self.type()
        print(type1)
    def showHeight(self):
        height1 = self.type()
        print(height1)
    def showLength(self):
        length1 = self.type()
        print(length1)
    def showWeight(self):
        weight1 = self.type()
        print(weight1)

class compGame(toy):
    def __init__(self):
        self.category = "racing"
        self.console = "PS4"

    def showCategory(self):
        category1 = self.type()
        print(category1)
    def showConsole(self):
        console1 = self.type()
        print(console1)





