import random

students_dict={}
students_list=['강경식', '권명은', '권오준', '공 혁', '김효승', '박제영', '이계윤', '조한근', '허서연']

while len(students_dict)<len(students_list):
    
    x=input("출첵 : ")
    if x not in students_list:
        print('????')
    elif x not in students_dict:
        y=random.choice(['네','안 온거 같아요'])
        print(y)
        if y=='네':
            students_dict[x]='O'
        else:
            students_dict[x]='X'
    else:
        print("이미 부르셨어요")
    

print("-------<출석명단>-------")
for i in range(len(students_dict)):
    print(f"{students_list[i]:<5} : {students_dict.get(students_list[i]):>5}")
print("------------------------")