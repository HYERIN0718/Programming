n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
cnt = 0
res = 0


for _ in range(m):
    if cnt == k:
        res += arr[1]
        cnt = 0
    else:
        res += arr[0]
        cnt += 1
print(res)
