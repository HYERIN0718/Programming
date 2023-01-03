import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

arr = []
for i in a:
    arr.append(i)

for i in b:
    arr.append(i)
arr.sort()

for j in arr:
    print(j, end=' ')
