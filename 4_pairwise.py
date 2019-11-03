arr = [1, 4, 2, 3, 0 , 5]
sums = 7
tlist = []
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if (i!=j) and ((arr[i] + arr[j+1]) == sums):
            if (i,j+1) not in tlist and (j+1,i) not in tlist:
                tlist.append((i,j+1))
                print("sum=", i+j+1)