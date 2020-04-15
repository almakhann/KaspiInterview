##Магазин
##10

def rec(i,t):
    if (i == 0):
        if(t == k):
            return 1
        else:
            return 0
    if(t + i<=k):
        if(a[i][t] == 0):
            a[i][t] += rec(i - 1, t + 1)
            a[i][t] += rec(i + 1, t + 1)
    return a[i][t]
            
text = input().split(' ')
k = int(text[1])
n = int(text[0])

a = [[0 for x in range(51)] for y in range(51)]


if(n % 2 == 0 and k % 2 == 1):
    print(0)
else:    
    for i in range(51):
        for j in range(51):
            a[i][j] = 0
    print(rec(n,0))
