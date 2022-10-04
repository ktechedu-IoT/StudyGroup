import random

#정답숫자 뽑기
def right_answer():               # 함수선언
    numbers = []                  # 세 가지 숫자를 담을 리스트 선언
    i = 0
    a = 0
    while i <3:
        a = random.randint(0,9)  
        print(a)
        if a not in numbers:      # 수가 문자열에 겹치지 않으면 숫자열에 추가
            numbers.append(a)
            i= i+1                # i 에 +1 넣는다 (i+1 X)
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았다.\n")
    return numbers

#숫자입력 및 예측
def my_count():
    print("숫자 3개를 하나씩 차례로 입력.")
    i = 0
    my = []
    while i <3:
        try:
            my_number = int(input(f"{i+1}번째 숫자를 입력하시오 : "))
            
            if my_number >9:       #범위를 정해줌
                print("범위를 벗어났습니다.다시입력해주세요")
                continue
            if my_number in my:      #중복된 수 를 판별하기 , my_number 가 my리스트에 있다면 중복 아니면 넣기
                print("중복되는 숫자입니다. 다시입력 : ")
            else:
                my.append(my_number)          #조건에 맞는 정수를 저장
                i= i+1
        except Exception as e:
            print("잘못입력했습니다. 숫자를 입력해주세요. ",e)   

            #예외처리를 하기 위해 try, except 사용 범위 숫자 범위와 다른 숫자 말고 문자열 입력시 처리를 위해서
            # 마지막 print 'e'  표시는 어떤게 예외처리인지   
    return my

#점수 판별
def score(a,b):                    # 함수 호출(score) 한것을 매개변수로 받음
    strike = 0
    ball = 0
    i = 0

    while i <len(a):
        if a[i] == b[i]:            # 위치와 값이 같을때
            strike +=1              # 스트라이크 카운팅 (0에서 +1)
            i += 1
        elif a[i] in b:             # 값은 있지만 위치가 다를 때
            ball += 1               # 볼 카운팅
            i += 1            
        else:                       # 둘다 다를때
            i = i+1
            
    return strike,ball

#코드 실행
answer = right_answer()
xx = 0
out = 0
while out !=3:
    
    guest = my_count()
    strike,ball = score(guest,answer)
    print(f"\n{strike} 스트라이크 : {ball} 볼\n")
                  
    if strike == 3:
        xx += 1  
        print(f"성공. {xx}번 만에 성공하였습니다.")
        break 
    
    if strike==ball==0:  
        out += 1
        xx += 1
        print('{} 아웃\n'.format(out))
    if out ==3:
        print("루저 ...\n")

    else:
        xx += 1
        