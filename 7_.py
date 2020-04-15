##Преобразование последовательности
##7

text1 = input()
text2 = input()

l = text2.split(' ')
dic = {}
max_s = 0
min_s = 0

for i in range(int(text1)):
    if l[i] in dic:
        dic[l[i]] = (dic[l[i]] + 1)
    else:
        dic[l[i]] = 1
    if dic[l[i]] > max_s:
        max_s = dic[l[i]]
        min_s = l[i]
    


for i in range(max_s):
    l.remove(min_s)
    l.append(min_s)

print(' '.join(l))
