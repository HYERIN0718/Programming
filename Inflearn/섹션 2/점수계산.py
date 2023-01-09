import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
score = 0
m = 0

for i in range(len(a)):
    if a[i] == 1:
        m += 1
        
        # 1이 나온 횟수만큼 최종 점수에 더함
        score += m
    elif a[i] == 0:
        m = 0
        score += m
print(score)
