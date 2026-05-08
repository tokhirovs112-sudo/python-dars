import os
os.system("cls")

n = int(input("Sonni kiriting: "))

yigindi = 0

for i in range(1, n + 1):
    print(i, end=" ")
    yigindi += i

print()
print("Yig'indi:", yigindi)