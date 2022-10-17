count=0
result1=0

def ch(a,b):
    tmp = str(a[1])+str(b[1])
    c=int(tmp)
    return c

def ch2(b):
    if len(b)>2:
        print("99를 초과 하였습니다")
    elif len(b)==1:
        b.insert(0,0)
    return b
    
num=int(input("숫자를입력하세요:"))
b=[int(a)for a in str(num)]
b=ch2(b)
print(num)
while result1 != num:
    sum2=b[0]+b[1]
    tmp=[int(a)for a in str(sum2)]
    tmp=ch2(tmp)
    result1=ch(b,tmp)
    print(b[0],"+",b[1],"=",sum2,"->",result1)
    b=[int(a)for a in str(result1)]
    b=ch2(b)
    count+=1
print(count,"번에 완료.")
        


