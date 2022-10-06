user = []
idw = []
pw = []
xx = True
      
while xx:
    try:
        print('---------------------')
        print('1.회원가입')
        print('2.확인')
        print('3.ID 찾기')
        print('4.패스워드 찾기')
        print('5.종료')
        print('---------------------\n')
        
        select = int(input('선택하시오 : '))
             
        if select == 1:                # 선택한 번호가 1번일때

            name = input('1.이름\n')
            new_id = input('2.id\n')
            password = input('3.비밀번호\n')
            
            user.append(name)
            idw.append(new_id)
            pw.append(password[::-1])       #역순을 만들때 reversed 를 안쓰는 이유는
                                            # 객체로 반환을 해줘서 한줄 추가로 변형은 가능
            
        if select ==2:
            print("~~~확인 결과~~~~\n")
            print(len(user))
            for i in range(len(user)):
                print("\n이름:",user[i])
                print("아이디:",idw[i])       
                print("비밀번호:",pw[i])
                print("--------------------\n")               

        if select == 3:
            
            a = input('이름을 입력하세요:')
            b = input('비밀번호를 입력하세요:')[::-1]
            print(b)
            if a == user and b == pw:
                print(f'id는 {idw} 입니다.')
            else:
                print('틀렸습니다. 다시 확인해주세요')

        if select == 4:
            c = input('이름을 입력하세요:')
            d = input('ID 를 입력하세요:')
            if c == user or d == idw:
                print(f'비밀번호는 {pw} 입니다')
            else:
                print('틀렸습니다. 다시 확인하세요')                     

        if select > 5:
            print("선택사항을 입력하세요. 다시입력하세요.")

        if select == 5 :
            print("종료합니다")
            break     

    except Exception as e:
        print("잘못 입력했습니다.",e)