import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
score = 0
m = 0

for i in range(len(a)):
    if a[i] == 1:
        m += 1
        score += m
    elif a[i] == 0:
        m = 0
        score += m
print(score)
