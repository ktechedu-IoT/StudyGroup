import random

def 판정(너, 상대):
    묵찌빠 = ['묵','찌','빠']
    if(묵찌빠.index(너) == 묵찌빠.index(상대)):
        return '비겼'
    elif((묵찌빠.index(너) - 묵찌빠.index(상대)) in [-1, 2]):
        return '이겼'
    else:
        return '졌'

#플레이횟수 = int(input('플레이횟수 : '))
플레이횟수 = 3 #일단 3세트로 고정
현재플레이횟수 = 0
진횟수 = 0
이긴횟수 = 0

while(이긴횟수<=플레이횟수//2 and 진횟수<=플레이횟수//2 and 현재플레이횟수<플레이횟수):
    너 = input('나 : ')
    상대 = random.choice(묵찌빠)
    print('상대 : ', 상대)
    승패 = 판정(너, 상대)
    현재플레이횟수 += 1
    print(f"{현재플레이횟수}회차 가위바위보에서 {승패}습니다.")
    if 승패 == '이겼':
        이긴횟수 += 1
    elif 승패 == '졌':
        진횟수 += 1

if 이긴횟수 > 진횟수:
    print("묵찌빠 게임을 이겼습니다.")
elif 이긴횟수 < 진횟수:
    print("묵찌빠 게임을 졌습니다.")
else:
    print("묵찌빠 게임을 비겼습니다.")
