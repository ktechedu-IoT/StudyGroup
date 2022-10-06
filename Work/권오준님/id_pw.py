import getpass  # 입력값 안보이게 하는법

info = []
i =0
while True:
    check = str(getpass.getpass("1. 회원가입\n2. 정보확인\n3. id 찾기\n4. pw 찾기\n5. 비밀번호 변경하기\n6. 나가기"))
    print("-"*40)
    if check == '1' or check == '회원가입':

        name = str(input("1-1. 이름 : "))
        while name == '':
            print("\n 필수입력 사항입니다.\n")
            name = str(input("1-1. 이름 : "))       
    
        id =  str(input("1-2. id : "))
        while id == '':
            print("\n 필수입력 사항입니다.\n")
            id =  str(input("1-2. id : "))
        
        pw = str(input("1-3. pw : "))
        while pw == '':
            print("\n 필수입력 사항입니다.\n")
            pw = str(input("1-3. pw : "))

        if name in info or id in info:
            print("\n이미 가입된 정보입니다. \n")
            name = str(input("1-1. 이름 : "))
            id =  str(input("1-2. id : "))
            pw = str(input("1-3. pw : "))
        
        info.append(name)
        info.append(id)
        info.append(pw[::-1])

        print("-"*40)
        
    elif check == '2' or check =='정보확인':
        for i in range(0,len(info),3) :
            print(f"이름 : {info[i]}, id : {info[i+1]}, pw : {info[i+2]}")
            print("-"*40)
        

    elif check == '3' or check =='id 찾기':
        id_name = str(input("이름을 입력하세요 : "))
        id_pw = str(input("pw를 입력하세요 : "))
        print("-"*40)
        while True:
            if id_name  not in info or id_pw[::-1] not in info:
                print("가입 정보가 없습니다.")
                print("-"*40)
                id_name = str(input("이름을 입력하세요 : "))
                id_pw = str(input("pw를 입력하세요 : "))
                print("-"*40)
            
            elif id_name in info and id_pw[::-1] in info: # reversed된 id_pw 값이 실제 비밀번호와 달라도  
                for i in range(0,len(info),3):            # info 안에 있는 값이라면 허용됌..ㅠ
                    if id_name == info[i]:
                        print(f"id : {info[i+1]}")
                        print("-"*40)
                break

    elif check == '4' or check =='pw 찾기':
        pw_name = str(input("이름을 입력하세요 : "))
        pw_id = str(input("id를 입력하세요 : "))
        print("-"*40)
        while True:
            if pw_name  not in info or pw_id not in info:
                print("가입 정보가 없습니다.")
                print("-"*40)
                pw_name = str(input("이름을 입력하세요 : "))
                pw_id = str(input("id를 입력하세요 : "))
                print("-"*40)
                
            elif pw_name in info and pw_id in info:     # pw_name과 pw_id의 입력값이 실제와 다르더라도
                for i in range(0,len(info),3):          # info 안에 있는 값이라면 허용됌..ㅠ
                    if pw_name == info[i]:
                        print(f"pw : {info[i+2][::-1]}")
                        print("-"*40)
                break
            
    elif check == '5' or check =='비밀번호 변경하기':
        change_id = str(input("id를 입력하세요 : "))
        print("-"*40)
        while True:
            if change_id not in info:
                print("가입 정보가 없습니다.")
                print("-"*40)
                change_id = str(input("id를 입력하세요 : "))
                print("-"*40)
                
            elif change_id in info:  
                change_pw = str(input("pw를 입력하세요 : "))
                print("-"*40)
                if change_pw[::-1] not in info:
                    print("가입 정보가 없습니다.")
                    print("-"*40)
                    change_pw = str(input("pw를 입력하세요 : "))
                    print("-"*40)

                elif change_pw[::-1] in info:
                    new_pw = str(input("새로운 pw를 입력하세요 : "))
                    print("-"*40)
                    for i in range(0,len(info),3):          
                        if change_id == info[i+1]:
                            del info[i+2]
                            info.insert(i+2,new_pw[::-1])      
                            print("비밀번호가 변경되었습니다.")     
                            print("-"*40)             
                    break
                    
    elif check == '6' or check == '나가기':
        break
