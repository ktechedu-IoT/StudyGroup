import random

student = ['a','b','c','d']
attend= dict.fromkeys(student)

def a_print(new_attend):
    print()
    abcd= "<<출석명단>>"
    print("-"*4, end="-")
    print(f"{abcd}",end="-")
    print("-"*4)

    for key,element in new_attend.items():  
        print(f"{key: <10}:{element:>10}")
    print("-"*22)
    print()

def a_check():
    while None in attend.values(): 
        x= input("학생이름을 부르세요>>>")
        if x not in student:
            print("누구죠?")
        else:
            if attend[x]==None:
                z=random.choice(["y", "n"])
                if z== "y":
                    print("네")
                    attend[x]= "o"
                else:
                    print("안 온것 같아요")
                    attend[x]= "x"
            else:
                print("이미 부르셨어요")
    new_attend = dict(sorted(attend.items()))
    a_print(new_attend)

a_check()