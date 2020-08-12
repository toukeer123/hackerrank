# hackerrank
some codes of hackerrank.
def twoStrings(s1, s2):
    z = 0
    for i in range(len(s1)):
        z = s2.find(s1[i])
        if(z>=0):
            return "YES"
    return "NO"

q = int(input())
for i in range(q):
    s1 = input()
    s2 = input()
    result = twoStrings(s1,s2)
    print(result)
