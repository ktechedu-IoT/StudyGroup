import random 

   
students_a = ['강경식', '권명은', '권오준', '공혁', '김효승', '박제영', '이계윤', '조한근', '허서연']
students_b = []
answers_c = ['네','안 온 거 같아요~']
answers_d = []
answers_e = []


i=0
while len(students_b)!=len(students_a):
    student = input()
    if student not in students_b:   
        if student in students_a :
            answers_d = random.choice(answers_c)
            print(answers_d)
            students_b.append(student)
            if answers_d == '네':
                answers_e.append('O')
            elif answers_d == '안 온 거 같아요~':
                answers_e.append('X') 
       
        else:
            print('?')
    else:
        print ('이미 부르셨어요~') 
    
print('-------------<출석명단>-------------')            
for i in range(len(answers_e)):      
    print(f'{students_b[i]} : {answers_e[i]}')
print('-----------------------------------')


   
  

  