a = []
bund = 0

for i in range(0, 10):
    print("enter a number")
    bund = int(input())
    a.append(bund)
    if i > 0:
        for r in range(i, 0, -1):
            numb = 0
            for y in range(0, r):
                if a[y] > a[y + 1]:
                    numb = a[y]
                    a[y] = a[y + 1]
                    a[y + 1] = numb
for i in range(0, 10):
    print a[i]