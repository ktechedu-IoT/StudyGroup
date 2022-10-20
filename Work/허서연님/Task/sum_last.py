import random as ran
import time
n = str(ran.randrange(1,100))

if len(n) < 2:
    n = n.zfill(2)
print(f'n = {n}')


a = n

print(a)
print(n)
i=0


while True:    

    b = str(int(a[0]) + int(a[1]))    
    print(b)
    number = str(a[1]) + b[-1]
    print(number)
    a=number
    print("b : ",b)
    print("a : ", a)
    print("number : ",number )
        
    i+=1
    if a==n:
        break

    print('a[0] : ',a[0])
    print('a[1] : ',a[1])
   
print(f'총 횟수는{i}입니다.')
