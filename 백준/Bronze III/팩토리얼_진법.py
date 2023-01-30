import sys

# 팩토리얼 함수
def factorial(n) :
    if n == 1:
        return 1
    return n * factorial(n-1)

# input() 말고 sys.stdin 모듈 사용하기
while True:
    num = sys.stdin.readline().strip()
    if int(num) == 0:
        break
    
    l = len(num)
    result = 0

    for i in range(l):
        result += int(num[i]) * factorial(l-i)
    print(result)
