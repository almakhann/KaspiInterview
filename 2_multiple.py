##Python 3.7.0
##Произведение цифр
##2

text = input()
a = int(text)

l = []
if a == 0:
    print('10')
elif a <= 9:
    print(str(a))
else:
    for i in reversed(range(2,10)):
        while(a % i == 0):
            l.append(str(i))
            a = a/i
    if(a != 1):
        print('-1')
    else:
        print((''.join(l))[::-1])
        


