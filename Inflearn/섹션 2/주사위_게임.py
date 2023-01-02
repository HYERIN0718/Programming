import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
arr = []
score = 0

for i in range(n):
   a = list(map(int, input().split()))
   for j in range(len(a) - 2):
       if a[j] == a[j+1] and a[j+1] == a[j+2]:
           score = 10000 + a[j] * 1000
           arr.append(score)
       elif a[j] == a[j+1] and a[j +1] != a[j+2]:
           score = 1000 + a[j] * 100
           arr.append(score)
       elif a[j] != a[j+1] and a[j+1] != a[j +2] and a[j] != a[j+2]:
            a.sort()
            score = a[j+2] * 100
            arr.append(score)

arr.sort()
print(max(arr))
