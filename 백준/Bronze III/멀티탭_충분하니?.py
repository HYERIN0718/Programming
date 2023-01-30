n, k = map(int, input().split())
arr = list(map(int, input().split()))
s = 0

for i in range(k):
    s += (arr[i] + 1) //2
if s >= n:
    print("YES")
else:
    print("NO")
