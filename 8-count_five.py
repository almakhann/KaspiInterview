##Пятерки
##8

def countForDigit(n):
    if ((n<=0)):
        return 0
    d = 5
     
    res = 0
    k = 10
    while(k==10 and ((n//k)>0) or (n//(k//10)>0)):
        if (k==10):
            if ((n % k) >= d):
                res = res + (n//k) + 1
            else:
                res = res + (n//k)
        else:
            if d>0:
                if (((n % k)//(k//10)) > d):
                    res+=(n//k)*(k//10) + k//10
                else:
                    if (((n % k)/(k//10)) == d):
                        res+=(n//k)*(k//10) + ((n % k) % (k//10))+1
                    else:
                        res+=(n//k)*(k//10)
            else:
                if ((n % k) >= (k//10)):
                    res = res + (max((n//k)-1, 0)*  (k//10) + min((n//k),1) * (k//10))
                else:
                    res = res + (max((n//k)-1, 0)*  (k//10) + min((n//k),1) * (n % (k//10)) + 1)
        k = k*10
    return res


row = input()
print(countForDigit(int(row)))
