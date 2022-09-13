import random

def ok ():
   names = ['강경식', '권명은', '권오준', '공혁', '김효승', '박제영', '이계윤', '조한근', '허서연']
   b = []
   d = []
   e =""
   c= ['네','안온것같아요']
   while len(b)!=len(names):
      a= input()
      if a not in b:
         if a in names:
            b.append(a)
            e = random.choice(c)
            print(e)
            if e=='네':
               d.append('o')
            else :
               d.append('x')
            e =""
         else :
            print('?')
      else :
         print("이미 부르셨어요")
   prin(b,d)

def prin(b,d):
   print("-------------<출석명단>-------------")
   for i in range(len(d)):
      print(b[i]+':'+d[i])
   print('------------------------------------')

ok()
   
   
      
      







