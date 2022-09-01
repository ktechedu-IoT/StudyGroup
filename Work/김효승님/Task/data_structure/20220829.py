import random

<<<<<<< HEAD
def 판정(self, enemy):
    if self=='묵':
        if enemy=='묵':
            Result='비김'
=======
def game(me, you):
    me1 = ["묵","찌","빠"]
    you1 = ["빠","묵","찌"]
    if me == you: 
        승패='비김'
    elif me not in me1: 
        승패='잘못'
    elif me1.index(me) == you1.index(you): 
        승패='졌'
    else:
        승패='이김'
    return 승패    
>>>>>>> 2e27e7055fefef6770413c0d5f1537734ce03360

        elif enemy=='찌':
            Result='이김'

        else:
            Result='짐'

    elif self=='찌':
        if enemy=='묵':
            Result='짐'

        elif enemy=='찌':
            Result='비김'

        else:
            Result='이김'

    elif self=='빠':
        if enemy=='묵':
            Result='이김'

        elif enemy=='찌':
            Result='짐'
            
        else:
            Result='비김'
    return Result    #Result는 '나'의 기준으로 작성됨


Result = '비김'
묵찌빠 = ['묵','찌','빠']
<<<<<<< HEAD



while Result == '비김':
    self = input('나 : ')
    enemy = random.choice(묵찌빠)
    print("enemy :",enemy)
    Result = 판정(self, enemy)
    if Result == '비김':
        print("가위바위보에서 비겼습니다.\n")

while Result != '비김':
    if Result == '이김':
        print("당신이 가위바위보에서 이겼습니다.\n")
    else:
        print("enemy가 가위바위보에서 졌습니다.\n")
    전판 = Result
        
    self = input('나 : ')
    enemy = random.choice(묵찌빠)
    print("enemy :",enemy)
    Result = 판정(self, enemy)

if 전판 == '이김':
    print("묵찌빠 게임을 이겼습니다.")
else:
    print("묵찌빠 게임에서 졌습니다.")
=======
승=0
무=0
패=0
while 1 :
    me = input('나 : ')
    you = random.choice(묵찌빠)
    print("상대 :",you)
    승패 = game(me, you)
    if 승패 == '비김':
        print("가위바위보에서 비겼습니다.")
        무+=1
    elif 승패 == '이김':
        print("당신이 가위바위보에서 이겼습니다.")
        승+=1
    elif 승패 == '잘못':
        print("잘못입력하였습니다. 종료하겠습니다")
        print("총판수:"+str(승+패+무)+" "+str(승)+ "승"+ str(무)+"무" +str(패)+"패")
        break
    else:
        print("상대가 가위바위보에서 졌습니다.")
        패+=1
   
>>>>>>> 2e27e7055fefef6770413c0d5f1537734ce03360
