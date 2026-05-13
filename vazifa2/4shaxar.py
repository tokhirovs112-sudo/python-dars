
ali = {"Toshkent", "Samarqand", "Buxoro", "Andijon"}
vali = {"Toshkent", "Farg'ona", "Buxoro", "Xiva"}

print("Ikkalasi ham borgan:")
for i in ali & vali:
    print(i)

print("Faqat Ali borgan:")
for i in ali - vali:
    print(i)