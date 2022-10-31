class Person:
    data=[]
    def __init__(self,name,gender,address,tel):
        self.name=name
        self.gender=gender
        self.address=address
        self.tel=tel

class Member(Person):
    def __init__(self,name="",gender="",address="",tel="",id="",pw=""):
        super().__init__(name,gender,address,tel)
        self.id=id
        self.pw=pw

    def join(self):
        b=1
        while b:
            a=1
            name = input("이름 : ")
            gender=input("성별 : ")
            address=input("주소 : ")
            tel=input("연락처: ")
            while a :
                id=input("id : ")
                a = Member.id_check(self,id)
            pw=input("pw : ")
            reg=Member(name,gender,address,tel,id,pw)
            b = Member.in_member(self,name,gender,address,tel)
        Person.data.append(reg)
    
    def __repr__(self):
        return  (f"[name={self.name!r},gendet={self.gender!r},address={self.address!r},tel={self.tel!r}]")

    def in_member(self,name,gender,address,tel):
        for i in range(len(Person.data)):
            if name == Person.data[i].name and gender == Person.data[i].gender and address== Person.data[i].address and tel== Person.data[i].tel:
                print("가입된 계정입니다")
                return 1
        return 0
        
    def id_check(self,tmp_id):
        for i in range(len(Person.data)):
            if tmp_id == Person.data[i].id:
                print("해당 id가 존재합니다")
                return 1
        return 0
        
        def print_menu():
    print("1. 회원 가입")
    print("2. 회원 확인")
    print("3. 수정")
    print("4. 탈퇴")
    print("5. id칮기")
    print("6. pw찾기")
    print("7. 종료")
    menu = input("메뉴선택: ")
    return int(menu)

def run():
    x=Member()
    while 1:
        menu = print_menu()
        if menu == 1:
            x.join()
        elif menu == 2:
            print(str(Person.data))
        elif menu == 3:
            x.modify()
        elif menu == 4:
            x.dellogin()
        elif menu == 5:
            x.findid()
        elif menu == 6:
            x.findpw()
        elif menu == 7:
            break
        
run()
        
