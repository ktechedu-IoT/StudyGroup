import random 

students_a = ['강경식', '권명은', '권오준', '공혁', '김효승', '박제영', '이계윤', '조한근', '허서연']
students_b = []
answers_c = ['네','안 온 거 같아요~']
answers_d = []
answers_e =[]

yesno = random.choice(answers_c)

i=0
while 1:
    student = input()
    if student in students_a:
        if student not in students_b :
            print(yesno)
            students_b.append(student)
            answers_d.append(yesno)   
            if student =='허서연':
                print('-------------<출석명단>-------------')            
                for i in range(0,len(students_b),1):
                    if answers_d[i]=='네':
                        answers_e.append('O')
                    elif answers_d[i]=='안 온 거 같아요~':
                        answers_e.append('X')              
                    print(f'{students_b[i]} : {answers_e[i]}')
                print('-----------------------------------')
                break
        elif student in students_b:
            print('이미 부르셨어요~') 
    elif student not in students_a:
            print('?')
    
        
   


  