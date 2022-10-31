
### 회원관리 자식클래스 최종완성판3(index ,try~except, 자식클래스변수를 __init__에 정의)
#                                (제명함수와 탈퇴함수를 remove함수로 통일, 변수e사용)
#                                (login id와 pw를 체크하는 각각의 함수정의)
#                                (super()함수 이용)

class Person:
    def __init__(self, name, id, pw, add, tel):
        self.name = name
        self.id = id
        self.pw = pw
        self.add=add
        self.tel=tel
    
    def __str__(self):        
        return self.name+" "+self.id+" "+self.pw+" "+self.add+" "+self.tel        
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other): 
        return self.id==other.id

class Member(Person):
    login_id = None
    index=0    
    choice=0
    condition=True
    
    def __init__(self,name="",id="",pw="",add="",tel=""):
        super().__init__(name, id, pw, add, tel)
        self.list= []
    
    def condition_state(self):
        if Member.condition== False:
            Member.condition=True
        
        
    def join(self):
        print("회원가입 절차입니다.")
        name=input(("이름을 입력하세요>>"))
        self.condition_state()
        while Member.condition:
            id=input("ID를 입력하세요>>>")
            self.join_idchk(id)
        self.condition_state()
        pw= input("password를 입력하세요>>")
        add=input("주소를 입력하세요>>")
        tel=input("전화번호를 입력하세요>>")
    
        member=Member(name, id, pw,add,tel)
        print("회원가입 완료 했습니다. 환영합니다.")
        self.list.append(member)
        print(self.list)
        
    def join_idchk(self,id):
        e=0
        for member in self.list:
            if (member.id== id):
                print("중복 id입니다")
                e=1
                break
        if e==1:
            pass
        elif e==0:
            Member.condition=False       
                 
        
    def login(self):
        if Member.login_id !=None:
            print("이미 로그인 상태입니다")
            return
        else:
            self.condition_state()
            while Member.condition:
                id=input("아이디를 입력하세요>>>")
                self.login_idchk(id)
            self.condition_state()
            while Member.condition:
                pw=input("패스워드를 입력하세요>>>")
                self.login_pwchk(pw)
            self.condition_state()
            print("로그인 성공입니다.")
            Member.login_id= id
            
    def login_idchk(self,id):                     
        e=0
        for member in self.list:
            if (member.id== id):
                e=1
                Member.condition=False
                
        if e==0:
            print("id가 틀립니다. 다시 입력하세요")
            

    def login_pwchk(self,pw):
        e=0
        for member in self.list:
            if (member.pw== pw):
                e=1
                Member.condition=False
                
        if e==0:
            print("pw가 틀립니다. 다시 입력하세요")          

    
    def logoff(self):
        if Member.login_id==None:
            print("로그인부터 하세요")
        else:
            Member.login_id = None
            print("로그오프 상태로 바뀌었습니다.")

    def view(self):        
        print("정보확인 절차입니다.")
        id=input("정보확인이 필요한 id를 입력하세요>>>")
        member=Member("",id,"","","")
        try:
            Member.index = self.list.index(member)
        except Exception as e:
            print("회원이 없거나 id를 잘못 입력했습니다.")
            self.view()
        else:
            print(self.list[Member.index])
                    
    def remove(self):
        if Member.choice==3:
            print("회원탈퇴 절차입니다.")
        else:
            print("회원제명절차입니다.")
        
        id=input("아이디를 입력하세요>>>")
        member=Member("",id,"","","")
        try:
            Member.index = self.list.index(member)
        except Exception as e:
            print("회원이 아니거나 id를 잘못 입력했습니다.")
            self.remove()
        else:
            del self.list[Member.index]
            print("명단삭제처리했습니다.")
            print(self.list)             
    
    def modify(self):
        print("수정 절차입니다.")
        self.login()
        id=Member.login_id
        choice = int(input("수정하고 싶은 항목을 고르세요>>1. pw 2.주소 3.전화번호>>>"))
                
        for member in self.list:
                if member.id==id:
                    match choice:            
                        case 1:
                            member.pw=input("새 패스워드>>")                     
                        case 2:
                            member.add = input("새 주소>>")                            
                        case 3:
                            member.tel = input("새 전화번호>>")                    
                    print(member)

               
    def operation(self):
        condition=True
        while condition:            
            print("********메뉴********")
            print("1: 회원가입2:로그인3:회원탈퇴4:회원제명", end='')
            print("5:회원view 6:정보수정 7:로그오프8:메뉴나감")
            try:
                Member.choice = int(input("원하시는 메뉴를 선택하세요:>>>"))
            except:
                print("sorry!! 메뉴번호가 아닙니다. 번호를 입력하세요")
                continue
            else:           
                if Member.choice>=9 or Member.choice==0:
                    print("메뉴에 없습니다.다시 선택하세요")
                    continue
                else:
                    match Member.choice:  
                        case 1: self.join()
                        case 2: self.login()
                        case 3: self.remove()
                        case 4: self.remove()
                        case 5: self.view()
                        case 6: self.modify()
                        case 7: self.logoff()
                        case 8: condition=False                     
          
def main():
    mem=Member()
    mem.operation()

main()
