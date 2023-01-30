n = int(input())
m = int(input())
s = m

for i in range(n):
    a, b = map(int, input().split())
    m = m + (a - b)
    if m < 0 :
        s = 0
        break
    elif m >= 0:
        if s <= m:
            s = m
print(s)
