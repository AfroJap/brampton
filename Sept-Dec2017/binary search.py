from random import randint

a = []
bund = 0

for q in range(0, 25):
    bund = int(randint(0, 9)+4)
    a.append(bund)

u = 0
numb = 0
for r in range(25, 0, -1):
    numb = 0
    for y in range(0, r-1):
        port = y + 1
        if a[y] > a[y + 1]:
            numb = a[y]
            a[y] = a[y + 1]
            a[y+1] = numb

for i in range(0, 25):
        print(a[i])