import os
os.system("cls")
nom=['apple', 5, True, 'apple', 'banana', 'google', 5, 'banana', False, 'banana']
list2 = []
for i in nom:
    if nom.count(i)>=2 and i not in list2:
       list2.append(i)
print(list2)