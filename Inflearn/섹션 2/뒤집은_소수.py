import sys
sys.stdin=open("input.txt", "rt")

# 각 자연수를 뒤집기
def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        
        # 뒤집기
        res = res * 10 + t
        x = x // 10
    return res

# 뒤집은 숫자가 소수인지 판별하기
def isPrime(x):
  
    # 1은 소수가 아니기 때문에 제외시킴
    if x == 1:
        return False
      
    # 소수는 입력받은 숫자의 절반까지 해당됨
    for i in range(2, x // 2 + 1):
        
        # x는 함수호출할 때 불러오기 때문에 따로 입력할 필요 없음
        if x % i == 0:
            return False
        else:
            return True

n = int(input())
arr = list(map(int, input().split()))

for x in arr:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end = ' ')
