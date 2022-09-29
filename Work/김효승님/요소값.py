import random

list=[]
maxnum=0
max =0
minnum=100
min =0
for i in range(10):
    randomnum = random.randrange(1,101)
    list.append(randomnum)
list.sort(reverse=True)
print(list)
for i in range(1,10,1):
    if maxnum < list[i-1]-list[i]:
        maxnum=list[i-1]-list[i]
        max=i
    if minnum > list[i-1]-list[i]:
        minnum=list[i-1]-list[i]
        min = 1
print(f"최대 {list[max-1]},{list[max]}")
print(f"최소 {list[min-1]},{list[min]}")

    
