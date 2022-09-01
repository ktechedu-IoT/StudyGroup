import random

def 판정(self, enemy):
    if self=='묵':
        if enemy=='묵':
            Result='비김'

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