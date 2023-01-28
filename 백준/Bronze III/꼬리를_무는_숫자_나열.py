n, m = map(int, input().split())

if n % 4 > 0:
    a = n // 4 + 1
    b = n % 4
else:
    a = n // 4
    b = 4

if m % 4 > 0:
    s = m // 4 + 1
    k = m % 4
else:
    s = m // 4
    k = 4

print(abs(a-s) + abs(b-k))
