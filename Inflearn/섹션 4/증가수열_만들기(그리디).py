import sys
sys.stdin=open("input.txt", "rt")      

n = int(input())
arr = list(map(int, input().split()))
tmp = []
lt = 0
rt = n - 1

# 수열 맨뒤의 값
last = 0
res = ""

while lt <= rt:
    if arr[lt] > last:
        tmp.append((arr[lt], 'L'))
    if arr[rt] > last:
        tmp.append((arr[rt], 'R'))
    tmp.sort()

    if len(tmp) == 0:
        break
    else:
        res = res + tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()
print(len(res))
print(res)
