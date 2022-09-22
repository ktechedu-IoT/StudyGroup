import random
a = int(input("ox 퀴즈 테스트 횟수"))
c=["O","X"]
resort=[]
def OX():
    a=[]
    for i in range(0,10,1):
        b = random.choice(c)
        a.append(b)
    return a

for i in range(a):
    e=OX()
    b=0
    d=0
    for i in e:
        if i == "O":
            b+=1
            d+=b
        else:
            b=0
    print(e,":",d,"점")
    resort.append(d)
    f=sorted(resort,reverse=True)
for j in range(0,3,1):
    print(j+1,"등 :",f[j])
