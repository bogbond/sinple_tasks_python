
def sIndexMin(arr, v):
    left = 0
    right = len(arr)-1

    while 1:
        center = (left + right) // 2
        if arr[left] == v:
            return left
        elif left - center==1:
            return None
        elif arr[center] < v:
            left = center + 1
        else:
            right = center - 1
    return None
    

def sIndexMax(arr, v):
    left = 0
    right = len(arr)-1
    count =1
    while 1:
        center = (left + right) // 2
        if arr[left] == v:
            while arr[left] == arr[left+count]:
                    count=count+1
            return(count+left-1)
        elif left - center==1:
            return None
        elif arr[center] < v:
            left = center + 1
        else:
            right = center - 1
    return None

    
def sum(arr, v):
    return sIndexMax(arr, v)-sIndexMin(arr, v)+1   #suppose that this nubrer is in the list
    


#    0  1  2  3  4   5   6   7   8   9   10  11  12  13  14  15  16 
a = [2, 2, 4, 8, 10, 10, 12, 15, 20, 56, 60, 60, 60, 75, 81, 81, 90]

example = 81

print(sIndexMin(a, example))
print(sIndexMax(a, example))
print(sum(a, example))