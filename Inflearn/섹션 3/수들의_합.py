import sys
sys.stdin=open("input.txt", "rt")

a, b = map(int, input().split())
arr = list(map(int, input().split()))
lt = 0
rt = 1
s = arr[0]
count = 0

while True:
    if s < b:
        if rt < a:
            s += arr[rt]
            rt += 1
            
        # rt가 n과 같아졌을 때 break
        else:
            break
    elif s == b:
        count += 1
        
        # 앞의 인덱스 값을 유지하기 위해 lt값을 삭제함
        s -= arr[lt]
        lt += 1
    else:
        s -= arr[lt]
        lt += 1
print(count)
