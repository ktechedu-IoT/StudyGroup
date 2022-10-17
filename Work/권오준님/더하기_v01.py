i=0
n=int(input("숫자를 입력하시오 : "))
number = n

while True:
    a = number//10  # 몫
    b = number%10   # 나머지
    c = (a+b)%10    
    number = (b*10)+c
    i+=1

    if number==n:
        break

    
print(f'총 횟수는{i}입니다.')
