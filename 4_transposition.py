##Перестановка
##4

row = input()
qw = row.split(' ')

text = []
for i in qw:
    text.append(i.lower())

first = list(text[0])
first.sort()

second = list(text[1])
second.sort()

if first == second:
    print('Yes')
else:
    print('No')


