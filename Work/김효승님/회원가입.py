print("1.로그인\n2.회원가입\n3.회원찾기\n4.종료")
num = input("메뉴를 알려주세요:")
Required=[['이름'],['아이디'],['페스워드'],['생년월일']]
quired=[['이메일'],['주소'],['나이']]
name =[]
id =[]
passwd=[]
dateofbirth=[]
email1=[]
address=[]
old=[]


def login():
    num=0
    ids = input("ID :")
    passwds = input("PASSWORD 입력 :")
    for i in range(len(id)):
        if id[i]==ids:
            num+=i
            passwdss=encryption(passwds)
            if passwd[i] == passwdss:
                print(name[i]+"님 환영합니다")
                num=+4
                return num 
            else :
                print("password가 틀렸습니다")
        else:
            print("해당id는 존재하지않습니다.")
    return num
            

def register():
    global name,id,passwd,dateofbirth,email1,address,old
    num=0
    print("*은 필수입력사항입니다.")
    tmp=input("이름*: ")
    if tmp != '':
        name.append(tmp)
    else:
        print("이름은 필수입력 사항입니다")
        tmp=input("다시입력하세요")
    
    tmp=input("ID*: ")
    if tmp != '':
        id.append(tmp)
    else:
        print("ID는 필수입력 사항입니다")
        tmp=input("다시입력하세요")
    
    tmp=input("PASSWD*: ")
    if tmp != '':
        tmp = encryption(tmp)
        passwd.append(tmp)
    else:
        print("PASSWD는 필수입력 사항입니다")
        tmp=input("다시입력하세요")
    
    tmp=input("생년월일*: ")
    if tmp != '':
        dateofbirth.append(tmp)
    else:
        print("생년월일은 필수입력 사항입니다")
        tmp=input("다시입력하세요")
    
    tmp=input("이메일:")
    if tmp == '':
        email1.append('')
    else:
        email1.append(tmp)
    
    tmp=input("주소: ")
    if tmp == '':
        address.append('')
    else:
        address.append(tmp)
    
    tmp=input("나이: ")
    if tmp == '':
        old.append('')
    else:
        old.append(tmp)
    return num

def encryption(password):
    global passwd
    tmp=list(password)
    tmp2=''
    for i in reversed(range(len(tmp))):
        tmp2+=tmp[i]
    return tmp2

def findid(named,bas):
    num = 0
    names=[]
    for i in range(len(name)):
        if named==name[i]:
            names.append(int(i))
    for i in names:
        if dateofbirth[i] == bas:
            print("ID는:",id[i])
            return num
    print("해당 정보로 가입된 회원이없습니다.")
    return num

def findpw(ids):
    num=0
    a=0
    for i in range(len(id)):
        if ids==id[i]:
            a=i
    tmp=decryption(a)
    print("passwd는",tmp)
    return num

def decryption(num):
    tmp =list(passwd[num])
    tmp2=''
    for i in reversed(range(len(tmp))):
        tmp2+=tmp[i]
    return tmp2

def test():
    print("1.id찾기\n2.passwd찾기\n3.뒤로가기: ")
    a=0
    num=input('메뉴를 알려주세요:')
    if num=='1' or num=='id찾기':
        name=input("이름을 입력하세요: ")
        bass=input("생년월일을 입력하세요")
        findid(name,bass)
    elif num=='2' or num=='passwd':
        ids=input("id를 입력하세요: ")
        findpw(ids)
    else:
        print("없는메뉴입니다")
        return a

while num !='4' or num=="종료":
    if num=='1' or num=='로그인':
        num=login()
    elif num=='2' or num=='회원가입':
        num=register()
    elif num=='3'or num=='회원찾기':
        num=test()
    elif num=='777':
        print(name,id,passwd,dateofbirth,email1,address,old)
        num=0
    elif num==0:
        print("1.로그인\n2.회원가입\n3.회원찾기\n4.종료")
        num = input("메뉴를 알려주세요:")
    elif num==4:
        break
    else:
        num=0







        
