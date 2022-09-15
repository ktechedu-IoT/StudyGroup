import random
randomnum = random.randrange(1,86401)

def nowtime():
    global randomnum
    nowhours = randomnum//3600
    nowminut = (randomnum//60)%60
    nowsec = randomnum%60
    return nowhours,nowminut,nowsec

def endtime(randomnum):
    if randomnum > 86400:
        randomnum-=86400
    nowhours = randomnum//3600
    nowminut = (randomnum//60)%60
    nowsec = randomnum%60
    return nowhours,nowminut,nowsec


a= nowtime()
print(a[0],'시',a[1],'분',a[2],'초')
randomtime= random.randrange(1,501)
print(randomtime,'초 증가')
endnum=randomtime+randomnum
b= endtime(endnum)
print("종료시간")
print(b[0],'시',b[1],'분',b[2],'초')