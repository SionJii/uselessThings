import random

print('난수의 개수를 입력하세요')
usrInput = int(input())

print("\n==== 난수의 숫자들 ====")

sum = 0
for i in range(usrInput):
    randomNum = random.randrange(1, 11)
    sum += randomNum
    print(randomNum, end='')
    if i == usrInput-1:
        break
    print(", ", end='')

print('\n==== 1~10 사이의 난수 4개의 합계 ====')
print(sum)
