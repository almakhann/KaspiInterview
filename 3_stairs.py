##Лестница
##3

row = input()

a = 0
last = 0
for i in range(1,int(row)+1):
    a += i
    if a <= int(row):
        last = i
print(last)
