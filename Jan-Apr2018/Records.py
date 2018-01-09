def FindLetter(dund):
    found = False
    while found == False:
        for i in range(0, 6):
            if a[i].nameID == dund:
                found = True
                position = [a[i].nameID, a[i].nodeID]
    return position

nullPtr = -1

class Node:
    def __init__(self):
        self.nameID = ""
        self.nodeID = 0

a = []

for i in range(0,6):
    a.append(Node())
    a[i].nodeID = i+1


a[0].nameID = 'h'
a[1].nameID = 'e'
a[2].nameID = 'l'
a[3].nameID = 'p'
a[4].nameID = 'm'
a[5].nameID = 'e'
a[5].nodeID = nullPtr

y = 0
for i in range(0,6):
    print(a[y].nameID)
    y = a[y].nodeID

bund = "h"

FoundLetter = FindLetter(bund)
print(FoundLetter)
