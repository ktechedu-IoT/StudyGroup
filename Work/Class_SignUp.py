class Person:
    def __init__(self,a,b,c,d,e):
        self.name=a
        self.gender=b
        self.age=c
        self.address=d
        self.telephone=e

class Member(Person):
    choice=0
    index=0
    login_id=None
    condition=True

    def __init__(self,na=" ",gen=" ",ag=" ",add=" ",tel=" ",f=" ",g=" "):
        super().__init__(na, gen, ag, add, tel)
        self.identity=f
        self.password=g
        self.data=[]

    def __str__(self):
        return self.name + " " + self.gender + " " + self.age + " " \
             + self.address + " " + self.telephone + " " + self.identity + " " \
             + self.password
    def __repr__(self):
        return self.__str__()

    def __eq__(self,other):
        return self.identity==other.identity

    def join(self):
        n=input("name>>>>>>>>")
        g=input("gender>>>>>>")
        a=input("age>>>>>>>>>")
        d=input("address>>>>>")
        t=input("telephone>>>")
        while Member.condition:
            i=input("ID>>>>>>>>>>")
            self.join_idchk(i)
        p=input("password>>>>")
        Member.condition=True
        member=Member(n,g,a,d,t,i,p)
        self.data.append(member)
        print(self.data)

    def join_idchk(self, jid):
        for j in self.data:
            if j.identity==jid:
                print("already Exist!!! Enter Again!!!")
                return
        Member.condition=False

    def login(self):
        if Member.login_id!=None:
            print("alredy login~! ")
            return            
        else:
            Member.condition=True
            while Member.condition:
                i=input("Enter ID>>>>>>")
                self.login_idchk(i)
            Member.condition=True
            while Member.condition:
                p=input("Enter Password>>>>>")
                self.login_pwchk(p)
            Member.condition=True
            print("Success Login!!!")
            Member.login_id=i             

    def login_idchk(self,lid):
        for l in self.data:
            if l.identity==lid:
                Member.condition=False
                return
            else:
                print("ID is wrong. Reenter Please!!")

    def login_pwchk(self,lpw):
        for l in self.data:
            if l.password==lpw:
                Member.condition=False
                return
            else:
                print("Password is wrong. Reenter please!!")

    def logoff(self):
        if Member.login_id==None:
            print("Start by Login!")
        else:
            Member.login_id=None
            print("Changed Logoff")

    def view(self):
        print("validate prodedure>>>>>")
        vid=input("Enter ID>>>>>>>>>")
        member=Member("","","","","",vid,"")
        try:
            Member.index=self.data.index(member)
        except Exception as e:
            print(" You do not have a member or you entered your ID incorrectly!")
            self.view()
        else:
            print(self.data[Member.index])

    def remove(self):
        print("deletion prodedure>>>>>")
        rid=input("Enter ID>>>>>>>>>")
        member=Member("","","","","",rid,"")
        try:
            Member.index=self.data.index(member)
        except Exception as e:
             print("You do not have a member or you entered your ID incorrectly!")
             self.remove()
        else:
            del self.data[Member.index]
            print("Deletion Complete!!")
            print(self.data)

    def modify(self):
        print("modifying procedure>>>>>>>>>")
        self.login()
        mid=Member.login_id
        choose=int(input("Choose>>>> 1.Password 2.Address 3.Telephone >>>>>>>"))

        for m in self.data:
            if m.identity==mid:
                match choose:
                    case 1:
                        m.password=input("Enter New Password>>>>")
                    case 2:
                        m.address=input("Enter New Address>>>>")
                    case 3:
                        m.telephone=input("Enter New Telephone>>>")
                print(m)

    def operation(self):
        Member.condition=True
        while Member.condition:
            print("------- Menu -------")
            print(" 1. SignUP 2. LogIn 3. withdrawal 4. Deletion", end='')
            print(" 5. Validate 6. Modifying 7. LogOff 8. Out")
            try:
                Member.choice=int(input("Choose One!>>>>>>"))
            except:
                print("Sorry!! Enter once again!!>>>>>>>")
                continue
            else:
                if Member.choice>=9 or Member.choice==0:
                    print("Not on the menu, please select again!>>>>")
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
                        case 8: Member.condition=False

# def main():
#     End=Member()
#     End.operation()

# x=Member()
# x.join()
# x.login()
# x.view()
# #x.remove()
# x.modify()
# x.operation()

mem=Member()
mem.operation()
