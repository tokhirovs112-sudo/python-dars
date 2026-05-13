set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
juft = set1.union(set2)

for i in juft:
    if i % 2 == 0:
        print(i, end=" ")