# DECLARE a : ARRAY[0..9] OF INTEGER

for q in range[0, 9]:
    print("Enter a whole number")
    a[q] = input()

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

for y in range(1, 11):
    print a[i]
    i = i + 1




# to loop from 9 down to 0:for index in range(9, -1, -1)