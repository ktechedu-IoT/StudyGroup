import random

xx = int(input("몇 게임 하시겠습니까>>?"))
a=0
temp=[]
lotto_Winner_number =[]

for j in range(6):
    a = random.randint(1,45)
    while a in lotto_Winner_number:              
        a = random.randint(1,45)
    lotto_Winner_number.append(a)
print("당첨번호==>>",sorted(lotto_Winner_number),"\n")
print(type(lotto_Winner_number))

lotto = [i for i in range(1,45)]
for i in range(xx):
    random.shuffle(lotto)
    print("자동번호!!:",sorted(lotto[0:6]))

    result = []
    for n in lotto_Winner_number:
        if n in lotto:
            result.append(n)
          
    if (lotto_Winner_number) == 3:              #lotto_winner_number
        print("5등")
    elif  (lotto_Winner_number) == 4:
        print("4등")
    elif  (lotto_Winner_number) == 5:
        print("3등")
    elif  (lotto_Winner_number) == 5: 
        print("2등")
    elif  (lotto_Winner_number) == 6:
        print("1등")
    else: print("꽝") 

    #아직 당첨번호와 자동번호를 비교하는것을 못한상태
    #리스트와 리스트를 비교 하려고 할 때 인덱스0,1,2 ... 순으로 비교를하고있어서
    #현재 계속 꽝이 나옴. 그것을 수정해야함.
    #다시 뽑아서 비교를 하든 다른식으로 하든 바꿔줘야함.
    