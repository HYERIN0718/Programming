import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000

for i in range(n):
    sum1=sum2=0
    for j in range(n):
        # 행 증가
        sum1+=a[i][j]
        # 열 증가
        sum2+=a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

sum1 = sum2 = 0
for i in range(n):
    # 대각선
    sum1 += a[i][i]
    # 대각선 반대 & j열 : n-i-1 (-1해줘야됨)
    sum2 += a[i][n-i-1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
        largest = sum2

print(largest)
