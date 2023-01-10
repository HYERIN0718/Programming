import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

# 회전
for i in range(m):
    b, c, d = map(int, input().split())
    for j in range(d):
        if c == 0:
            # pop(0) : 0번 인덱스 값 출력
            a[b-1].append(a[b-1].pop(0))
        else:
            # pop() : 마지막 인덱스 값 출력
            a[b-1].insert(0, a[b-1].pop())

            
count = 0
s = 0
e = n - 1 

# 모래시계 모양 값 출력
for i in range(n):
    for j in range(s, e+1):
        count += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1 
print(count)
