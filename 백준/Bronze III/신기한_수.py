n = int(input())
cnt = 0

for i in range(1, n+1):
    s = list(map(str, str(i)))
    k = 0
    for x in s:
        k += int(x)
    if i % k == 0:
        cnt += 1
print(cnt)
