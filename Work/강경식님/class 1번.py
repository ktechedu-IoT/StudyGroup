# class zoo:
#     def __init__(self, name, age, at, dt, pe):
#         self.name = name
#         self.age = age
#         self.at = at
#         self.dt = dt
#         self.pe = pe

# p1 = zoo('양', 27, 100, 50, '온순')
# p2 = zoo('악어', 19, 500, 30, '사납')

# print(f"이름은:{p1.name} 나이는:{p1.age} 공격력은: {p1.at} 방어력은:{p1.dt} 성격은:{p1.pe}\n")
# print(p2.name,p2.age,p2.at,p2.dt,p2.pe)

# # class Car:
# #     def __init__(self,바퀴,가격):
# #         self.바퀴 = 바퀴
# #         self.가격 = 가격

# # car = Car(2, 1000)
# # print(car.바퀴)
# # print(car.가격)

class Monster:
    m_list = []
    def __init__(self, name, age, at, dt, pe):
       
        self.name = name
        self.age = age
        self.at = at
        self.dt = dt
        self.pe = pe
        

    def input_info(self):
        name = input("이름:")
        age = int(input("나이:"))
        at = int(input("공격력:"))
        dt = int(input("방어력:"))
        pe = input("성격:")

    def say(self):
        
        while(True):
            num = int(input("1.기존등록동물보기, 2.새로 생성하기, 3.종료 >>"))
            if num == 1 == zoo:
                self.ani()
            if num == 2:
                self.input_info()
            else:
                num == 3
                break                
                
zoo = [
("늑대",5,500,60,"온순"),

("호랑이", 8, 800, 300, "용맹"),

("판다", 15, 1, 1, "태평"),

("토끼", 4, 2, 0, "귀엽")]