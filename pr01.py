
arr = [5, 7, 2, 8, 14, 4, 23, 27, 3, 7, 26, 10]
max_d = 0

for itemE in arr[::-1]:
    for itemF in arr:
        if itemE > itemF:
            if itemE - itemF > max_d:
                max_d = itemE - itemF

print(max_d)

