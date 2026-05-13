
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

natija = (set1 - set2) | (set2 - set1)

for i in range(9, 0, -1):
    if i in natija:
        print(i, end=" ")