import random as ran

batter = []
while len(batter) != 3:
    swing = ran.randint(0,9)
    if swing not in batter:
        batter.append(swing)
print(batter)

o=0

while True:
    s=0
    b=0
    
    pitching = input('숫자를 입력하세요 :').split()
    pitching = list(map(int,pitching))
   
    if len(set(pitching) & set(batter)) == 0:
        print("OUT!!")
        o +=1
        if o == 3:
                print("\n게임에 졌습니다!!")
                break

    for i in range(3):
        if pitching[i] in batter:
            if pitching[i] == batter[i]:
                s+=1     
            elif pitching[i] != batter[i]:
                b+=1     
    if s==3:
        print("\n게임에 승리했습니다!!")
        break
   
    print(f"{pitching} : {s}S, {b}B, {o}O")

   

       
   
       