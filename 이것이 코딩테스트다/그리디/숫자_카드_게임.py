n, m = map(int, input().split())
a = []

for i in range(n):
    arr = list(map(int, input().split()))
    arr.sort()
    a.append(arr.pop(0))

print(max(a))
