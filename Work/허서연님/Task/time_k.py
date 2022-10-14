import random as ran

a = ran.randrange(0,25)
b = ran.randrange(0,60)
c = ran.randrange(0,60)
d = ran.randrange(1,500)

print(f'현재시간은 {a}시 {b}분 {c}초')
print(f'경과시간은 {d}초')

e=c+d

if e>59:
    E=e%60
    B=b+(e//60)

elif b>59:
    B=b%60
    A=a+(b//60)

elif a>24:
    a=0


print(f'종료시간은 {a}시 {B}분 {E}초\n\n')