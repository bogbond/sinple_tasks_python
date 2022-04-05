arr = [0, 12, 11, 0, 28, 0, 5, 3, 5, 0]

for i in range(len(arr)):
    if arr[i] == 0:
        del arr[i]
        arr.append(0)
print(arr)



arr1 = [0, 12, 11, 0, 28, 0, 5, 3, 5, 0]
counter = 0

for el in arr1:
    if el == 0:
        counter=counter+1
        arr1.remove(0)
for i in range(counter):
    arr1.append(0)
    
print(arr1)



arr2 = [0, 12, 11, 0, 28, 0, 5, 3, 5, 0]
N = len(arr2)
for i in range(N-1):
    for j in range(N-i-1):
        if arr2[j] == 0:
            arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
 
print(arr2)