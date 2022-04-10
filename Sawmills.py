num = input()
data = input() # "tgggtt"

if (len(data) % 2 or (data.count('t') != data.count('g'))):
    print("NIE")
else:
    arr = []
    for i, l in enumerate(data):
        if i not in arr:
            arr.append(i)
            tmp = 0
            for j, c in enumerate(data[i+1:]):
                if l != c and tmp == 0:
                    if c == 'g':
                        arr.insert(len(arr)-1, j+1+i)
                    else:
                        arr.append(j+1+i)
                    break
                elif l == c:
                    tmp += 1
                else: 
                    tmp -= 1               
    countT = 1
    countG = 1
    help = []
    for i in data:
        if i == 't':
            help.append(countT)
            countT += 1
        else:
            help.append(countG)
            countG += 1
        
    for i in range(len(arr)//2):
        print(help[arr[i*2]], help[arr[i*2+1]])