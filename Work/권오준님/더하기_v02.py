n=str(input("숫자를 입력하시오 : "))


if int(n)<10:
    n='0'+n
number=n[1] + str(int(n[0]) + int(n[1]))[-1]

a=n
b=number
i=0

while True:
    
    b = a[1] + str(int(a[0]) + int(a[1]))[-1]
    a = b[0]+b[1]
    i+=1
    
    if a==n:
        break

print(f'총 횟수는{i}입니다.')