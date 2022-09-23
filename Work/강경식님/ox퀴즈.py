from operator import index
import random

xx = int(input("테스트 횟수는?>>"))
cho = ['o','x']
result = []
ranking= []

for i in range(xx):
    point = 0
    score = 0    
    result=[]
    for j in range(0,10):
        a = random.choice(cho)     
        result.append(a)

    for h in range(len(result)):
        if result[h] == 'o':
            point += 1
            score += point
        elif result[h] == 'x':
            point = 0
      

    print("-"*50)
    print(f"{result} : {score}점 입니다.")
    print("-"*50)

    ranking.append(score)
    ranking.sort(reverse=True)
print("등수닷\n")    
    
for q in range(3):
    print(f'{q+1}등 : {ranking[q]}점')   
print("-"*50)
        