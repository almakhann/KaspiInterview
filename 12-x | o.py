##Python 3.7.0
##Крестики-нолики ##12


lt=[]
for i in range(3):
    row = input()
    lt.append(row)

result = "Draw"
for i in range(3):
    row = 0
    colum = 0
    r_diag = 0
    l_diag = 0
        
    for j in range(3):
        row += ord(lt[j][i])
        colum += ord(lt[i][j])
        r_diag += ord(lt[j][j])
        l_diag += ord(lt[j][~j])
                
    if row == 264 or colum == 264 or r_diag == 264 or l_diag == 264:
        result = "Win"
    elif row == 237 or colum == 237 or r_diag == 237 or l_diag == 237:
        result = "Lose"

            
print(result)
    
    

