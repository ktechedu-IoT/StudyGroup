class Student:                              # 1번

    count = 0
    students = []
    
    @classmethod   #데코레이터
    def a(cls):                                                 #6번
        print("===================== 학생목록 =========================")
        print("이름\t국어\t영어\t수학\t과학\t총점\t평균\t등수\t등급")
        print()
        for student in cls.students:                            #7번
            print(student)
        print("========================================================")             #11번
        print (f"\n총 인원은{Student.count}명이다.\n")           #12번

    def __init__(self, name, kor, math, eng, sci):               #3번
        self.name = name
        self.kor = kor
        self.math = math
        self.eng = eng
        self.sci = sci
    

        Student.count +=1                                       #4번 카운팅해주고
        Student.students.append(self)                           #5번 지금 만든 목록을 리스트에 넣어줌
        
        
    def total(self):                                            #9번
        return self.kor + self.math + self.eng + self.sci
        

    def avg(self):                                              #10번
        return self.total()/4

    def ranking(self):
        return
       
                                       
    def grade(self):
        if self.avg() <= 100 and self.avg() >= 88:
            return("A")
        if self.avg() <= 88 and self.avg() >= 76:
            return("B")
        if self.avg() <= 76 and self.avg() >= 65:
            return("C")
        if self.avg() <= 65 and self.avg() >= 54:
            return("D")
        if self.avg() <= 54 and self.avg() >= 40:
            return("E")    
        if self.avg() <= 40 and self.avg() >= 0:
            return("F")
                           

    def __str__(self):                                  #오버라이딩 , 8번(object)
    #객체를 문자열로 반환 한다.
    #__str__ >> interface 로서 역할 수행, 서로 다른 타입을 가진 데이터끼리 문자열로 변환시켜 상호간의 호환 
    #__repr__ >>객체를 문자열로 표현. 반화값 eval함수에 사용가능,
    # 새로운 객체를 만들수 있다고 함 , __str__은 eval함수에 사용불가   
        return (f"{self.name}  {self.kor}\t{self.math}\t{self.eng}\
       {self.sci}\t{self.total()}\t{self.avg()}\t{self.ranking()}\t  {self.grade()}")
        

Student("카리나",84,86,75,99)                                # 2번
Student("우기  ",90,56,76,78)
Student("미연  ",91,92,76,77)
Student("장원영",95,97,80,89)
Student("신세경",96,93,99,83)
Student("사나  ",70,89,95,95)
Student("김효승",50,25,74,36)
Student("권오준",55,60,80,31)
Student("강경식",22,29,34,37)


Student.a()                                                #13번