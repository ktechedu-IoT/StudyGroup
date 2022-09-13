d = "## 출석부 만들기 ##"
def print_Title():
    print()
    print("="*70)
    print(d.center(65))
    print("="*70)

import random

students = ['강경식', '권명은', '권오준', '공혁', '김효승', '박제영', '이계윤', '조한근', '허서연']
qwer = []
values = []
check = ['네','안 온 거 같아요']

while True:
    
    xx = input("이름을 입력해주세요>>")

    if  xx not in qwer:
        if xx in students:
            a=random.choice(check)
            print(a)
            qwer.append(xx)
            values.append(a)
            print(qwer)
            print(values)
            if len(qwer) == 9:

                print_Title()
                print("\n--------출석명단---------\n")

                for i in range(len(students)):
                    if values[i]=='네':
                        print("{} : {} ".format(qwer[i],'o')) 
                    else:
                        print("{} : {} ".format(qwer[i],'x')) 
                    
                print("\n------------------------\n")
                break       
                
        else: 
            print('?')
    else:
        print("이미있습니다.")

# 좀 더 간단하게 만들고 싶었지만 시작이 이상했던건지 모르겠음다.
# 깔끔하게 할수있도록 해보겠습니다. 저는 아직 쉽지않네요...   