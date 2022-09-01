import random

choice = {1:"가위", 2:"바위", 3:"보", 4:"가위", 5:"바위"}
win =0
defeat=0
draw = 0
round = 0
i = 0

turn = int(input ("몇 번 가위 바위 보 하시겠습니까?>>>>"))

def win_or_defeated(user, com):
    global win, defeat, draw,i
    
    if user > com:
        win +=1
        return "승리하였습니다!!!"
    elif user < com:
        defeat +=1
        return "패배하였습니다ㅠㅠ"
    elif user==com: 
        draw +=1
        return "비겼습니다~"

def continue_confirm():
    while True:
        user = input("\n다시 하시겠습니까? : 네, 아니요 >>>>")
        if user=="네":
            return True
        elif user=="아니요":
            return False
        else:
            print("네 또는 아니요 를 입력해주세요")

while True:
    print(f"{i+1}라운드입니다")
    user= int(input("가위(1) 바위(2) 보(3) 중 하나를 선택하세요>>>>"))
        
    if  user == 1:
        com = random.choice([3,4,5])
        print(f"user:({choice[user]} vs {choice[com]}):com")
        print(win_or_defeated(4, com))
        i+=1
    elif user == 2:
        com = random.choice([1,2,3])
        print(f"user:({choice[user]} vs {choice[com]}):com")
        print(win_or_defeated(2, com))
        i+=1
    elif user == 3:
        com = random.choice([2,3,4])
        print(f"user:({choice[user]} vs {choice[com]}):com")
        print(win_or_defeated(3, com))
        i+=1
    elif user not in choice:
        round-=1
        print("다시입력바랍니다.")
    round+=1
        
    if i>=turn:
        if continue_confirm():
            continue
        else:
            break

print(f"총{round} 라운드 승패결과: {win}승 {draw}무 {defeat}패")