# DECLARE a : ARRAY[0..9] OF INTEGER
a = []
bund = 0
for q in range(0, 10):
        print("Enter a whole number, 0 < range > 11")
        bund = int(input())
        while bund < 0 or bund > 10:
            print("Error")
            print("Enter a whole number, 0 < range > 11")
            bund = int(input())
        a.append(bund)


u = 0
numb = 0
for r in range(9, 0, -1):
    numb = 0
    for y in range(0, r):
        if a[y] > a[y + 1]:
            numb = a[y]
            a[y] = a[y + 1]
            a[y+1] = numb

for i in range(0, 10):
    print a[i]




# to loop from 9 down to 0:for index in range(9, -1, -1)