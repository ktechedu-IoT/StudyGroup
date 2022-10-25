'''
1번)

class를 사용하여

동물들을 만들어보자. (4마리정도)

간단하게 동물이름, 나이, 공격력, 방어력, 성격의 값을 생성

ex) print = 늑대 의 나이는 5 살이고, 공격력은 200이며, 방어력은 100이고, 성격은 따뜻하다 

일단 클래스의 기본적인것을 만들어봄.
print 하는 방법은 한가지가 아니라 여러개가 있으므로 모두 다른식으로 나올수있음.
'''

class animal:
    def __init__(self,name,age,a,b,s):
        self.name = name
        self.age = age
        self.a = a
        self.b = b
        self.s = s

    def info(self):
        print(self.name,"의 나이는",self.age,"살이고, 공격력은",self.a,"방어력은",self.b,"성격은",self.s,"하다")


a=animal('늑대',5,200,100,'따뜻')
a.info()
b=animal('사자',5,200,100,'따뜻')
b.info()
c=animal('호랑이',5,200,100,'따뜻')
c.info()
b=animal('고양이',5,200,100,'따뜻')
b.info()

'''
학생의 리스트

kor, math, eng, sci 의 값을 넣어 총점과 평균값을 구해내보자.
ex)
Student("카리나",84,86,75,99)
Student("우기  ",90,56,85,88)
Student("미연  ",91,92,76,77)
Student("장원영",95,97,80,89)
Student("신세경",96,93,99,83)
Student("사나  ",70,89,95,95)

+ 클래스 변수를 사용하여 학생이 몇명인지 표시하기.
	총 인원은 { } 명이다.
	
==================== 학생목록 ========================
이름    국어    영어    수학    과학    총점    평균  

카리나  84      86      75      99      344     86.0  
우기    90      56      85      88      319     79.75 
미연    91      92      76      77      336     84.0  
장원영  95      97      80      89      361     90.25 
신세경  96      93      99      83      371     92.75 
사나    70      89      95      95      349     87.25 
======================================================

총 인원은6명이다.

++)추가내용

total 점수 등수 확인 / 잘하시는분들은 각 과목에 등수 확인 까지

하시면 좋고 안하시면 뭐 그럴수도 있고 <加油>
'''
'''
class Student:
    def __init__(self):
        self.name=[]
        self.kor=[]
        self.math=[]
        self.eng=[]
        self.sci=[]
        self.total=[]
        self.avg=[]
        self.rak=[]
    def push(self,name,kor,math,eng,sci):
        self.name.append(name)
        self.kor.append(kor)
        self.math.append(math)
        self.eng.append(eng)
        self.sci.append(sci)
        self.total.append(kor+math+eng+sci)
        self.avg.append((kor+math+eng+sci)/4)

    def rank(self):
        for i in range(0,len(self.avg)):
            ra=1
            for j in range(0,len(self.avg)):
                if self.avg[i] < self.avg[j]:
                    ra+=1
            self.rak.append(ra)
    
    def show(self):
        print("==================== 학생목록 ========================")
        print("이름\t국어\t영어\t수학\t과학\t총점\t평균")
        for i in range(len(self.avg)):
            print(self.name[i],"\t",self.kor[i],"\t",self.math[i],"\t",self.eng[i],"\t",self.sci[i],"\t",self.total[i],"\t",self.avg[i])
        print("======================================================")
    
    def rankshow(self):
        print("==================== 학생목록 ========================")
        print("이름\t국어\t영어\t수학\t과학\t총점\t평균\t등수")
        for i in range(len(self.avg)):
            print(self.name[i],"\t",self.kor[i],"\t",self.math[i],"\t",self.eng[i],"\t",self.sci[i],"\t",self.total[i],"\t",self.avg[i],"\t",self.rak[i])
        print("======================================================")
                            

student=Student()
student.push("카리나",84,86,75,99)
student.push("우기  ",90,56,85,88)
student.push("미연  ",91,92,76,77)
student.push("장원영",95,97,80,89)
student.push("신세경",96,93,99,83)
student.push("사나  ",70,89,95,95)
student.show()
student.rank()
student.rankshow()
'''

class Student:
    line=[]
    def __init__(self,name,kor,math,eng,sci):
        self.line.append([name,kor,math,eng,sci])
    
    @staticmethod
    def show(self):
        print("==================== 학생목록 ========================")
        print("이름\t국어\t영어\t수학\t과학\t총점\t평균")
        for i in range(len(self.avg)):
            print(self.name[i],"\t",self.kor[i],"\t",self.math[i],"\t",self.eng[i],"\t",self.sci[i],"\t",self.total[i],"\t",self.avg[i])
            print("======================================================")


Student("카리나",84,86,75,99)
Student("우기  ",90,56,85,88)
Student("미연  ",91,92,76,77)
Student("장원영",95,97,80,89)
Student("신세경",96,93,99,83)
Student("사나  ",70,89,95,95)
Student.show()



