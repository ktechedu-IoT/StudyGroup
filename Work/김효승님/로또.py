import random
total={"1등":0,"2등":0,"3등":0,"4등":0,"5등":0,"꼴등":0}
winning=(random.sample(range(1,45),6))
bonus=random.randint(1,45)
while bonus in winning :
    bonus=random.randint(1,45)

def compare(num):
    global total
    count=0
    result=set(num)&set(winning)
    if bonus not in num:
        count=len(result)
        if count == 6:
            total["1등"]+=1
            return 1
        elif count > 2  :
            total[str(8-count)+"등"]+=1
            return 8-count
        else :
            total["꼴등"]+=1
            return "꼴"
    else :
        count=len(result)+1
        if count == 6:
            total["2등"]+=1
            return 2
        elif count > 2 :
            total[str(8-count)+"등"]+=1
            return 8-count
        else :
            total["꼴등"]+=1
            return "꼴"

def auto():
    num=int(input("자동횟수 : "))
    for i in range(num):
        looto=random.sample(range(1,45),6)
        a= compare(looto)
        print(f"{looto} : 결과 {a}등") 

        
def manual():
    looto=[]
   
    while len(looto)<6: 
        num1 = int(input(f"{len(looto)+1}번째 번호를 입력해주세요"))
        if num1>45 :
            print("숫자가 너무 큽니다")
        elif num1 not in looto :
            looto.append(num1)
        else:
            print("중복값입니다.")
    a= compare(looto)
    print(f"{looto} : 결과 {a}등") 



print("1. 자동\n2. 수동\n3. 종료")
a=int(input("구매하실려는 번호를 눌러주세요: "))

if a == 1 :
    auto()
    print("당첨번호 :",winning)
    print("보너스볼 :",bonus)
    print(total)
if a == 2 :
    manual() 
    print("당첨번호 :",winning)
    print("보너스볼 :",bonus)
    print(total)
else:
    print("종료되었습니다.")