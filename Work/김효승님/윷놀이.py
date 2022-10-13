import random

a=['도','개','걸','윷','모']
pan=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]
pan1=[10,13,16,19,25,30,35,40]
pan2=[20,22,24,25,30,35,40]
pan3=[30,28,27,26,25,30,35,40]

savea=[]
keep=[]
total=[]
num=0
count=0
we=0
people =0
def ccc(choice):
    a=0
    if choice == "도":
        a+=1
    elif choice == "개":
        a+=2
    elif choice == "걸":
        a+=3
    elif choice == "윷":
        a+=4
    elif choice == "모":
        a+=5
    return a
num = int(input("횟수 : "))
people = int(input("인원 : "))

while we <people:
    savea.append(0)
    keep.append(0)
    total.append(0)
    we+=1
while count < num*people:
    try:
        for i in range(people):
            print(i+1,"선수")
            choice=random.choice(a)
            print(choice)
            cc=ccc(choice)
            savea[i]+=cc
            cc=savea[i]
            if keep[i]==0:
                print("현재말위치:",pan[cc])
                total[i]+=pan[cc]
                print("총점수 : ",total[i])
            elif keep[i]==1:
                print("현재말위치:",pan1[cc])
                total[i]+=pan1[cc]
                print("총점수 : ",total[i])
            elif keep[i]==2:
                print("현재말위치:",pan2[cc])
                total[i]+=pan2[cc]
                print("총점수 : ",total[i])
            elif keep[i]==3:
                print("현재말위치:",pan3[cc])
                total[i]+=pan3[cc]
                print("총점수 : ",total[i]) 
            if pan[cc]== 10 and keep[i] ==0:
                keep[i]=1
                savea[i]=0
            elif pan[cc]==20 and keep[i] ==0:
                keep[i]=2
                savea[i]=0
            elif pan[cc]==30 and keep[i] ==0:
                keep[i]=3
                savea[i]=0
            print("실행횟수:",count+1)
            count+=1
    except Exception as err:
        print("출발 지점으로 돌아갑니다")
        keep[i]=0
        savea[i]=0
        count+=1

