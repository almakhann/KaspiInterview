##Python 3.7.0
##Ферзь, ладья и конь
#1

text = input().split(' ')

table = "ABCDEFGH"

hf = table.find(text[0][0]) + 1
gf = int(text[0][1])

hl = table.find(text[1][0]) + 1
gl = int(text[1][1])

hk = table.find(text[2][0]) + 1
gk = int(text[2][1])

a = [[0 for x in range(9)] for y in range(9)]
for i in range(9):
    for j in range(9):
        a[i][j] = 0

for i in range(9):
    for j in range(9):
        if(i == 0 or j == 0):
            continue
        if(i == hf or j == gf):
            a[i][j] = 1
        if(abs(i - hf) == abs(j - gf)):
            a[i][j] = 1
        if(i == hl or j == gl):
            a[i][j] = 1
        if(abs((hk - i) * (gk - j)) == 2):
            a[i][j] = 1
a[hk][gk] = 0
a[hl][gl] = 0
a[hf][gf] = 0
count = 0
for i in range(9):
    for j in range(9):
        if(i == 0 or j == 0):
            continue
        if(a[i][j] == 1):
            count+=1
print(count)
