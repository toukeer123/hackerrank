# hackerrank
some codes of hackerrank.
def compareTriplets(a, b):
    x = [0,0]
    j = 0
    for i in range(len(a)):
        if(a[i]>b[i]):
            x[0] += 1
        if(a[i]<b[i]):
            x[1] +=1
        else:
            j=j+1
    return x

a = list(map(int,input().split()))
b = list(map(int,input().split()))
result = compareTriplets(a,b)
print(result)
