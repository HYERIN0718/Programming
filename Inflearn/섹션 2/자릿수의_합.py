import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

# 각 자연수의 자릿수의 합을 구하는 함수
def digit_sum(x):
    Sum = 0
    
    # 입력받은 자연수를 string으로 변환
    for i in str(x):
        Sum += int(i)
    return Sum

Max = -2147000000    
for x in a:
    total = digit_sum(x)
    if total > Max:
        Max = total
        
        # 출력값 res
        res = x

print(res)
