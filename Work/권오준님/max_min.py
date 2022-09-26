import random as ran

number =[]
diff = []
for i in range(10):
    n = ran.randint(1,100)
    number.append(n)
    
number.sort()
for i in range(0,10,2):
    diff.append(number[i+1]-number[i])


for i in range(5):
    if diff[i] == min(diff):
        a = number[2*i],number[2*i+1]
    elif diff[i] == max(diff):
        b = number[2*i],number[2*i+1]


print(number)
print(diff)
print()
print("거리 최소의 순서 쌍 :",a)
print("거리 최소의 순서 쌍 :",b)