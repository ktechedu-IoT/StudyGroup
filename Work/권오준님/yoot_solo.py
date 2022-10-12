import random as rd

users = int(input("몇명이 참가할지 정하시오 : "))
times = int(input("몇번 던질지 정하시오 : "))

map_a = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
map_b = [10, 13, 16, 19, 25, 30, 35, 40, 0]
map_c = [20, 22, 24, 25, 30, 35, 40, 0]
map_d = [30, 28, 27, 26, 25, 30, 35, 40, 0]

a=0
b=0
c=0
d=0
total=[]

while True:

    for i in range(0,times):
        
        if a!=5 and a!=10 and a!=15:
            yoot_1 = rd.randint(1,5)
            a+=yoot_1
              
            if a>20:
                a=0 
                total.append(0)
            else:
                total.append(map_a[a])
           
            print('yoot:', yoot_1)
            print('a:',a)
            print('b:',b)
            print('c:',c)
            print('d:',d)
            print('total:',total)

        elif a == 5 :
            
            yoot_2 = rd.randint(1,5)
            b+=yoot_2
               
            if b>=8:
                b=0
                a=0
                total.append(0)
            else:
                total.append(map_b[b])
            
            print('yoot:', yoot_2)
            print('a:',a)
            print('b:',b)
            print('c:',c)
            print('d:',d)
            print('total:',total)
            
        elif a==10:
           
            yoot_3 = rd.randint(1,5)
            c=yoot_3+c
            
            if c>=7:
                c=0
                a=0
                total.append(0)
            else:
                total.append(map_c[c])
            
            print('yoot:', yoot_3)
            print('a:',a)
            print('b:',b)
            print('c:',c)
            print('d:',d)
            print('total:',total)

        elif a==15:
            
            yoot_4 = rd.randint(1,5)
            d+=yoot_4

            if d>=8:
                d=0
                a=0
                total.append(0)
            else:
                total.append(map_d[d])
         
            print('yoot:', yoot_4)
            print('a:',a)
            print('b:',b)
            print('c:',c)
            print('d:',d)
            print('total:',total)

    break
       
print(f"\n윷놀이 최종 결과 : {sum(total)}점")

   

