import sys
sys.stdin=open("input.txt", "rt")      

n = int(input())
arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

# a를 내림차순으로 정렬
arr.sort(reverse=True)

largest = 0
res = 0

# a를 정렬했기 때문에 b만 비교하면 됨
for x, y in arr:
    if y > largest:
        largest = y
        res += 1
print(res)
