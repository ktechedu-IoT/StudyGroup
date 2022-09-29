import random

end=0

def count(num,b):
    s=0
    c=0
    o=0
    global end
    for i in range(0,3,1):
        if num[i] == b[i]:
            s+=1
        else:
            for j in range(0,3,1):
                if num[i] == b[j]:
                    c+=1
                else:
                    o+=1
    if o==9:
        end+=1
    if s==3:
        return 승리
    if end==3:
        return print("3진 아웃",b)
    return print(s,"s ",c,"b ",end,"o")



b= random.sample([0,1,2,3,4,5,6,7,8,9],3)
while True:
    num = list(map(int,input("숫자 3개 입력해주세요: ")))
    c=count(num,b)
    if c == "승리":
        print("승리하였습니다")
        break
