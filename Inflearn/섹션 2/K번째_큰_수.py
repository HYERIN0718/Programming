import sys
sys.stdin=open("input.txt", "rt")

a, b = map(int, input().split())
arr = list(map(int, input().split()))

# 집합 set
res = set() 

for i in range(a):
    for j in range(i + 1, a):
        for k in range(j + 1, a)
            res.add(arr[i] + arr[j] + arr[k]) # add() : set 집합에 값을 추가함

res = list(res)
res.sort(reverse=True)

print(res[b - 1])
