import sys
sys.stdin=open("input.txt", "rt")      

def Check(len):
  
    # 첫 번재 말
    count = 1
    
    # 말이 마지막으로 배치되는 지점
    ep = arr[0]
    for i in range(1, a):
        if arr[i] - ep >= len:
            count += 1
            ep = arr[i]
    return count
       

a, b = map(int, input().split())
arr = []

for i in range(a):
    tmp = int(input())
    arr.append(tmp)
arr.sort()

lt = 1
rt = arr[a-1]

while lt <= rt:
    mid = (lt + rt) // 2
    if Check(mid) >= b:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
