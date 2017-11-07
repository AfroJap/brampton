# DECLARE a : ARRAY[0..9] OF INTEGER
a = []

for q in range(0, 10):
    print("Enter a whole number")
    a.append(input())

u = 0
numb = 0
for r in range(9, 0, -1):
    numb = 0
    for y in range(0, r):
        port = y + 1
        if a[y] > a[y + 1]:
            numb = a[y]
            a[y] = a[y + 1]
            a[y+1] = numb

for i in range(0, 10):
    print a[i]




# to loop from 9 down to 0:for index in range(9, -1, -1)