# DECLARE a : ARRAY[0..9] OF INTEGER

lQ = "bum"
a = [7, 5, 6, 4, 9, 10, 8, 3, 1, 2]
i = 0

for y in range(1, 11):
    print a[i]
    i = i + 1

u = 0
numb = 0
for y in range(1, 100):
    port = u + 1
    if a[u] > a[u + 1]:
        a[u] = numb
        a[u] = a[u + 1]
        a[u+1] = numb
    u = u + 1

for y in range(1, 11):
    print a[i]
    i = i + 1
input()