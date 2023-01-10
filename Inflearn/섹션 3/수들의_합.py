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
            
            # s값은 lt ~ rt-1 인덱스의 값 까지의 합
            s += arr[rt]
            rt += 1
            
        # rt가 n과 같아졌을 때 break
        else:
            break
    elif s == b:
        count += 1

        # 인덱스 값을 증가시키면서 새로운 경우의 수를 구하기 위해 lt값을 삭제(초기화)함
        s -= arr[lt]
        lt += 1
    else:
        s -= arr[lt]
        lt += 1
print(count)
