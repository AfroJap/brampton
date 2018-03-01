class triangle:
    # Private a : INTEGER
    # Private h : INTEGER

    def __init__(self):
        self.a = 4
        self.h = 5

    def showArea(self):
        # DECLARE area :  REAL
        area = (self.a*self.h)/2
        print(area)

class square:
    # Private 1 : INTEGER

    def __init__(self):
        self.one = 4

    def showArea(self):
        # DECLARE are : REAL
        area = (self.one*self.one)
        print(area)


objects = [triangle(), square(), square(), triangle(), square()]

for i in range(0, 5):
    objects[i].showArea()

# show the area for each of the above items in the objects array

triOne = triangle()

triOne.showArea()
