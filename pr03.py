# arr = [5, 2, 8, 14, 4, 23, 27, 3, 7, 26, 10, 5, 7, 2, 8, 27, 3, 7, 26, 10]
arr = [1, 2, 2, 2, 3, 3, 5, 6, 7]
counter=0
d = {}

for i in range(len(arr)):
    if arr[i] in d:
        d[arr[i]]=1
    else:
        d[arr[i]]=0
    
for key, value in d.items():
    if value == 0:
        counter=counter+1
print("quantity of numbers occurring only once: ",counter)


print("amount of unique numbers (excluding repetitions)",len(list(set(arr))))