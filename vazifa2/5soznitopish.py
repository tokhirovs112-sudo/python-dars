
soz1 = input()
soz2 = input()

if len(soz1) != len(soz2):
    print(False)

else:
    harf1 = set(soz1)
    harf2 = set(soz2) #shu joyida AI ishlatdim

    if harf1 == harf2:
        print(True)
    else:
        print(False)