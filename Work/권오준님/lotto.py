import random as ran

n = int(input('로또 산 횟수 : '))

winning_num = []
auto_result=[]

while len(winning_num) !=6:
    a = ran.randint(1,45)
    
    if a not in winning_num:
        winning_num.append(a)

while len(winning_num) !=7:
    bonus = ran.randint(1,45)

    if bonus not in winning_num:
        winning_num.append(bonus)

winning_num.sort()

print('당첨번호 :',winning_num)
print('보너스 번호 :', bonus)
print('-'*50)

i = 0

while len(auto_result) != n:

    number =  []

    while len(number) != 7:
        random = ran.randint(1,45)

        if random not in number:
            number.append(random)
        
        number.sort()  

    auto_result.append(number)
    set_number = set(number)
    set_winning_num = set(winning_num)

    if len (set_number.intersection(set_winning_num)) <=2:
        print(f'{auto_result[i]} : 꽝')  
    elif len (set_number.intersection(set_winning_num)) == 3:
        print(f'{auto_result[i]} : 5등')  
    elif len (set_number.intersection(set_winning_num)) == 4:
        print(f'{auto_result[i]} : 4등')     
    elif len (set_number.intersection(set_winning_num)) == 5:
        print(f'{auto_result[i]} : 3등')
    else:  
        print(f'{auto_result[i]} : 1등')
        if bonus in number[i]:
            print(f'{auto_result[i]} : 2등')
    
    i+=1    




