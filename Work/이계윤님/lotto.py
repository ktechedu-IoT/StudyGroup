import random as rad

l = rad.sample(range(1,46),7)
*a,bonus = l
Lotto=set(a)

sl = input("1>>수동 로또 원하는 번호를 입력해주세요 : ").split()
self_lotto=set(map(int, sl))
print(f"1>>내가 구매한 수동 로또 : {self_lotto}")
j = self_lotto&Lotto
print(f"1>>수동 로또 당첨된 번호:{j}")
if len(j)==6:
    print("1등 입니다$$$$$\n")
elif len(j)==5:
    print("2등 입니다!!!!!\n") if bonus in self_lotto else print("3등 입니다!!!!!\n")
elif len(j)==4:
    print("4등 입니다~~~~~\n")
elif len(j)==3:
    print("5등 입니다~~~~~\n")
else:
    print("꽝!!! ㅠㅠ\n")

print("="*60)
print(f"로또 당첨번호 >>>> {Lotto}, 보너스번호 >>>> {bonus}")
print("="*60)

n=int(input("2>>자동 로또를 몇개 구매하시겠습니까? >>>> "))
for i in range(n):    
    m = rad.sample(range(1,46),6)
    auto_lotto=set(m)    
    print(f"2>>내가 구매한 자동 로또 : {auto_lotto}")    
    k = auto_lotto&Lotto        
    print(f"2>>자동 로또 당첨된 번호:{k}")
    if len(k)==6:
        print("1등 입니다$$$$$\n")
    elif len(k)==5:
        print("2등 입니다!!!!!\n") if bonus in auto_lotto else print("3등 입니다!!!!!\n")
    elif len(k)==4:
        print("4등 입니다~~~~~\n")
    elif len(k)==3:
        print("5등 입니다~~~~~\n")
    else:
        print("꽝!!! ㅠㅠ\n")
