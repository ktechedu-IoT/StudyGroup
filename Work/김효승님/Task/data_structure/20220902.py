#공백 제거 및 오류 코드 및 2진수 변환
def Blank(nums):
    remove_set=' '
    tmp=''
    blank=[i for i in nums if i not in remove_set]
    if blank[0]=='b':
        for j in blank[1::]:
            if j.isalpha():
                return 'a'
            else :
                tmp += j
            b = format(int(tmp), 'b')
        return 'c',b
    for j in blank:
        if j.isalpha():
           return 'a'
    for k in range(0,len(blank),1):
        if blank[k]=='/' and blank[k+1]=='0':
            return 'b'
    
    return blank

# 숫자 분류
def convers(num):
    numberring = []
    sign=[]
    conver = ''
    for k in num:
        if k.isdigit():
            conver+=k
        else:
            numberring.append(int(conver))
            sign.append(k)
            conver=''
    numberring.append(int(conver))
    return numberring,sign

#계산하기
def calcu(nums):
    blank=Blank(nums)
    if blank=='a':
        return "non-numeric value Error"
    elif blank=='b':
        return "divided by zero Error"
    elif blank[0]=='c':
        return blank[1]
    number=convers(blank)[0]
    arithm=convers(blank)[1]
    result=0
    j=0
    k=0
    if k ==0 :
        #곱하기 나누기 먼저계산
        for i in range(0,len(arithm),1): 
            if arithm[i]=='*' or '/' :
                if arithm[i]=='*':
                    result = number[i] * number[i+1]
                    number.pop(i+1)
                    number.pop(i)
                    arithm.pop(i)
                    k+=1
                    break
                elif arithm[i] == '/':
                    result = number[i] / number[i+1]
                    number.pop(i+1)
                    number.pop(i)
                    arithm.pop(i)
                    k+=1
                    break
    if k ==0 :
        #더하기 빼기 먼저계산
        for l in range(0,len(arithm),1): 
            if k==0 and arithm[l]=='+' or '-' :
                if arithm[i]=='+':
                    result = number[i] + number[i+1]
                    number.pop(i+1)
                    number.pop(i)
                    arithm.pop(i)
                    k+=1
                    break
            elif arithm[i] == '-':
                result = number[i] - number[i+1]
                number.pop(i+1)
                number.pop(i)
                arithm.pop(i)
                k+=1
                break
    while not number ==[] and k==1:
        #곱하기 계산
        for i in range(0,len(arithm),1):
            if arithm[i]=='*':
                result *=number[i]
                number.pop(i)
                arithm.pop(i)
                break
            elif arithm[i] == '/':
                result /= number[i]
                number.pop(i)
                arithm.pop(i)
                break
        if  '*' or '/' not in number :
            #더하기 빼기 계산
            if arithm[j] == '+':
                result += number[j]
                number.pop(j)
                arithm.pop(j)
            elif arithm[j] == '-':
                result -= number[j]
                number.pop(j)
                arithm.pop(j)
    if type(result)==float:
        return int(result * (10**4))/(10**4)
    return result
        
num = input()
result = calcu(num)
print(result)


