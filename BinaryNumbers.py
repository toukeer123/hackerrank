# hackerrank
some codes of hackerrank.
n = int(input())
res = [int(i) for i in bin(n)[2:]]
    
#print(res)
count = 0
out = []
if(n>=1):
    count =1
z = 0
y = 1
#print(y)
#print(z)
for i in range(len(res)):
    if(res[i]==1):
        count = count+1
        out.append(count)
    else:
        count = 1

print(max(out)-1)
