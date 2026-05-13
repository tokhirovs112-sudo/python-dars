tuple1 = (2, 3, 4, 5, 1, 8, 7)
juft=0
toq=0
for i in range(len(tuple1)):
    if tuple1[i]%2==0:
        juft+=tuple1[i]
    else:
        toq+=tuple1[i]

print("Juftlar yig'indisi: ", juft)
print("Toqlar yig'indisi: ", toq)