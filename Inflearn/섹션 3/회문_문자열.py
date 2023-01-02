import sys
sys.stdin=open("input.txt", "rt")

n = int(input())

for i in range(1, n + 1):
    a = input()
    
    # 대소문자 구별 없어야 하므로 모든 문자를 대문자로 변환
    a = a.upper()

    b = a[::-1]
    
    answer = 0
  
    if a == b:
        answer = 'YES'
    else:
        answer = 'NO'
        
    print("#%d" %i, answer)
