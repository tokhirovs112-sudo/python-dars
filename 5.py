for i in range(10, 100):
    sanoq = 0

    for j in range(1, i + 1):
        if i % j == 0:
            sanoq += 1

    if sanoq == 2:
        print(i, end=" ")