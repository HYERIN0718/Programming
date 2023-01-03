import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
count = 0

# s는 시작점, e는 종료점
s = e = n//2

for i in range(n):
    for j in range(s, e+1):
        count += arr[i][j]
    
    # i가 n//2보다 더 작으면 시작점은 더 작아지고, 종료점은 더 커짐
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(count)
