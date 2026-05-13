set1 = {"Artel", "Alif", "Yandex", "Google", "Meta"}
set2 = {"Google", "Apple", "Amazon", "Meta"}
set3 = {"Alibaba", "Uzum", "Meta", "Google", "Amazon"}

set4 = set1.intersection(set2)
set1.difference_update(set2,set3)
print("Hamma setda mavjud: ", set4)
print("Faqat birinchi setda mavjud: ",set1 )