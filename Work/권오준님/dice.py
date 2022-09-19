'''

주사위게임(3개의 주사위)


참가자 : x명

# 상금 
1. 같은수 3개 - 10000원 + 같은숫자 x 1000원
2. 같은수 2개 - 1000원 + 같은숫자 x 1000원
3. 다 다른경우 - 큰 수 x 1000원


------------------------------------
참가자 x명
[1, 1, 1] : a원
[2, 2, 2] : b원
    .
    .
[5, 5, 5] : e원
--------------------------------------
<가장 많은 상금 : b원>
'''


import random

# users=[]
# sub = []
s=[]
total=[]
money = []
user = int(input('참가인원 : '))
j=0
mon=0



for i in range(user):    
    value=[]   # value 리스트의 위치가 for문 안쪽으로 들어와야하는 이유?
    for j in range(3):
        dice = random.randrange(1,7)
        value.append(dice)
    total.append(value)
    
     
    
    if len(set(total[i])) ==1:
        # mon = (total[i]) * 1000 + 10000 / TypeError: can only concatenate list (not "int") to list --> 됐다 안됐다 하는 이유..?
        mon = max(total[i]) * 1000 + 10000
        money.append(mon) 
        s.append(set(total[i]))
    
    elif len(set(total[i])) ==2:  
        s.append(set(total[i]))
        #mon = max(total[i]) * 1000 + 1000  --> ..?
        money.append(mon)
        #sub =[i for i in total[i] if i not in s[i]] / listA - listB 안됌..
        
    else:
        mon = max(total[i]) * 1000
        money.append(mon)
        s.append(set(total[i]))
    
    


print('-'*40)
for i in range(user):
    print('{}:{}'.format(total[i],money[i]))
    
print('-'*40)
print('<가장 많은 상금 :{}원>'.format(max(money)))
   
#print(money)
#print(s)



        
