import random

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

승패 = '비김'
묵찌빠 = ['묵','찌','빠']
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
   