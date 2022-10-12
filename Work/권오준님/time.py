# 현재시간 + (1~500)초 --> ??

import random

a=int(random.randrange(0,24))
b=int(random.randrange(0,60))
c=int(random.randrange(0,60))
print("현재시간은: {}시 {}분 {}초 ".format(a,b,c))

d=int(random.randrange(0,500+1))
print('증가시간',d,'초')

if (c+d)>=60:
    b+=1   
elif 59<(c+d) and (c+d)<120:
    b+=2

print("종료시간은: {}시 {}분 {}초 ".format(a,b,c))
    

