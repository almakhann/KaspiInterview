##Обмен пакетами
##11

import math
text = []
for i in range(5):
    row = input()
    text.append(row)
  
  
a = 0
l = []
for i in range(1,len(text)):
    if text[i] == 'Time out':
        a += 1
    else:
        b = text[i].find('=')
        l.append( int((text[i])[b+1:]) )
  
print('Ping statistics for '+text[0][5:]+':')
print('Packets: Sent = 4 Received =',(4-a),'Lost =',(a),'('+str(25*a)+'% loss)')
  
if len(l) > 0: 
    average = math.ceil(sum(l)/len(l))
    print('Approximate round trip times:')
    print('Minimum =',min(l),'Maximum =',max(l),'Average =','{:d}'.format(average))
