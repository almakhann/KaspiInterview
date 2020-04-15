##Модуль суммы
##5


row1 = input()
data = input().split(' ')

pos = {}
neg = {}
zero = 0



for i in range(int(row1)):
    if int(data[i]) > 0:
        pos[i+1] = int(data[i])
    elif int(data[i]) == 0:
        zero += 1
    else:
        neg[i+1] = abs(int(data[i]))


result = ''
if sum(pos.values()) > sum(neg.values()):
    print(len(pos))
    for i in pos:
        result += str(i)+' '
    print(result)
elif zero == len(data):
    print('0')
else:
    print(len(neg))
    for i in neg:
        result += str(i)+' '
    print(result)
    
