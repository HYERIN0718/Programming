import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

ave = (sum(a) / n) + 0.5 # round() 함수 삭제
a = int(a)

aMin = 2147000000

for idx, x in enumerate(a):
    
    # tmp : (배열값 - 평균값)의 절대값
    tmp = abs(x - ave)
    if tmp < aMin :
        aMin = tmp
        
        # score : 배열값
        score = x 
        
        # res : 인덱스
        res = idx + 1
        
        
    elif tmp == aMin:
        
        # 크기비교가 1개 밖에 없는 이유 : score에 저장된 배열값과 새로운 x 배열값이 같다면 인덱스가 더 작은 숫자만 저장되기때문에 
        if x > score:
            score = x
            res = idx + 1

print(ave, res)
