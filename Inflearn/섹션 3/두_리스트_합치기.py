import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0
c=[]

# p1이나 p2 둘 중 하나라도 n, m 과 같아질 때까지 반복함
while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

# n이 m보다 크다면 a리스트가 남아있고 m이 n보다 크다면 b리스트가 남아있으므로 각각 c배열에 추가함
if p1 < n:
    c = c + a[p1:]
if p2 < m:
    c = c + b[p2:]

for i in c:
    print(i, end = ' ')


# 내가 푼 답 (sort()로 풀게되면 nlogn횟수 반복하므로 비효율적임)
'''arr = []
for i in a:
    arr.append(i)

for i in b:
    arr.append(i)
arr.sort()

for j in arr:
    print(j, end=' ')'''
