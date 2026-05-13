
set1 = {4,5,6,7,8,9}
set2 = {5,6,7,10,11}

a = 0
b = 0

for i in (set1 - set2) | (set2 - set1):
    a += i

for i in set1 & set2:
    b += i

print(a - b)