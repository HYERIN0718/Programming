k = int(input())
n = int(input())
s = 0

for i in range(n):
    t, z = map(str, input().split())
    if z == 'T':
        if s <= 210:
            k += 1
            if k > 8:
                k = 1
            s += int(t)
            if s > 210:
                print(k-1)
    elif z == 'N' or z == 'P' :
        if s <= 210:
            k += 0
            s += int(t)
            if s > 210:
                print(k)
