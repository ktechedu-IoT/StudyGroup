import random

list=[]
maxnum=0
minnum=100
for i in range(10):
    randomnum = random.randrange(1,101)
    list.append(randomnum)
list.sort(reverse=True)
print(list)
for i in range(1,10,1):
    if maxnum < list[i-1]-list[i]:
        maxnum=i
    if minnum > list[i-1]-list[i]:
        minnum=i
print(f"최대 {list[maxnum-1]},{list[maxnum]}")
print(f"최대 {list[minnum-1]},{list[minnum]}")

    
