import random

students_list=['a','b','c','d']
students_dict=dict.fromkeys(students_list)

while None in students_dict.values():
    x=input("출첵 : ")
    if x not in students_list:
        print('????')
    else:
        if students_dict.get(x)==None:
            y=random.choice(['네','아니요'])
            print(y)
            if y=='네':
                students_dict[x]='O'
            else:
                students_dict[x]='X'
        else:
            print("이미 부르셨어요")

print("-------<출석명단>-------")
for i in range(len(students_list)):
    print(f"{students_list[i]:<5} : {students_dict.get(students_list[i]):>5}")
print("------------------------")
