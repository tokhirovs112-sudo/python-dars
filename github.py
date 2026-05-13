import os
os.system ("cls")

tuple1 = ("Salom", "Hello", 1, 2, 3)

print(tuple1)
print(tuple1[3]) # 3 indeks dagi son

tuple1 = (1,2,3,4,5,6,7,8,9)
print(tuple1[3:]) # 3 indeksdan keyingi sonlar
print(tuple1[:5]) # 5 indeksgacha sonlarni va 5 indeks kirmaydi
print(tuple1[2:6]) # 2 va 6 indeksdagi sonlar oralig`idagi sonlarni chiqaradi
print(tuple1[1:8:2]) # 1 va 8 ideksdagi sonlari chiqaradi va 1 tadan tashab ketadi
print(tuple1[-2]) # orqadan sonni 2 indeksini korsatadi
print(tuple1[::-1]) # oxiridan boshigacha boradi
