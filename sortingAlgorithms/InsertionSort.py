arr = [2,23,1,45,10,34,67]

for i in range(1,len(arr)):
    j = i
    while j > 0 and arr[j-1] > arr[j]:
        arr[j],arr[j-1] = arr[j-1],arr[j]
        j-=1

print(arr)