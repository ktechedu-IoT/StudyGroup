import random

peple = int(input("참가자 인원"))
j=1
tep=0
joy=[]
def mone(money):
    tmp = {}
    for value in money:
        if value in tmp:
            tmp[value]+=1
        else:
            tmp[value] = 1
    sorttmp = sorted(tmp.keys(),reverse=True)
    for key,value in tmp.items():
        if value == 3:
            mon = key*1000+10000
        elif value == 2:
            mon = key*1000+1000
        if value == 1:
            mon =sorttmp[0]*1000
           
    return mon

while j<=peple:
    for i in range(0,3,1):
        a= random.randint(1,6)        
        joy.append(a)
    b = mone(joy)
    print(joy,":",b,"원")
    joy=[]
    if tep <= b:
        tep = b
    j+=1
print("<가장 많은 상금:",tep,"원>")
    










