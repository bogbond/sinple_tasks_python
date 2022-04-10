arr = [5,15,9,3,4]
# arr=[32, 44 ,3, 54, 53, 34, 23, 54, 67, 34, 2, 7, 3, 65, 7, 66, 65, 68, 70, 71, 46, 3, 54, 34, 32, 45]
d = {}
d=dict(enumerate(arr))

sorted_dict = {}
sorted_keys = sorted(d, key=d.get, reverse=False)  

for w in sorted_keys:
    sorted_dict[w] = d[w]

# print(arr,"\n\n\n")
# print(sorted_dict)

large = sorted_dict.popitem()
a = sorted_dict.popitem()
b = sorted_dict.popitem()
c = sorted_dict.popitem()


def pr(el1, el2):
    print(el1,"+",el2)
    print(el1+el2)

if large[0] != a[0]+1 and large[0] != a[0]-1:
    pr(large[1], a[1])
elif large[0] != b[0]+1 and large[0] != b[0]-1:
    pr(large[1], b[1])
else:
    pr(large[1], c[1])




