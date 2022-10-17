xx = input("숫자입력 (1~99)>>")
if int(xx) < 10:                    # 10보다 작으면 xx 앞에 0을 붙인다.
    xx = "0" + xx                     # 한자리 일 경우 앞에 문자열로 '0'을 붙이게함.

numbers = xx[1] + str(int(xx[0]) + int(xx[1]))[-1] # 문자열로 바꾸고 6 + (2 + 6) 인데
                                        # (str 안에 더한 값이 두자리면 [-1]위치에 값을 붙여라)
print(numbers)
print("----")
count = 1

while numbers != xx:          # numbers 와 xx 가 같지않으면 계속
    numbers = numbers[1] + str(int(numbers[0]) + int(numbers[1]))[-1]
    print(numbers)
    print("----")
    count += 1

print(f"총 횟수 {count}번 이다")