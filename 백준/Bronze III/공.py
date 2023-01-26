n = int(input())

s = [0, 1, 0, 0]
for i in range(n):
    a, b = map(int, input().split())
    s[a], s[b] = s[b], s[a]
for i in range(1, 4):
    if s[i] == 1: print(i)

# 내가 푼 답
'''
n = int(input())
x = 1
y = 0
z = 0

for i in range(n):
    a, b = map(int, input().split())

    if a == 1 and b == 2:
        x, y = y, x
    elif a == 1 and b == 3:
        x, z = z, x
    elif a == 2 and b == 1:
        y, x = x, y
    elif a == 2 and b == 3:
        y, z = z, y
    elif a == 3 and b == 1:
        z, x = x, z
    elif a == 3 and b == 2:
        z, y = y, z
if max(x, y, z) == x:
    print(1)
elif max(x, y, z) == y:
    print(2)
else:
    print(3) '''
