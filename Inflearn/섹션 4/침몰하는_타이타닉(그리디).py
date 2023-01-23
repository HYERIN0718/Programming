import sys
sys.stdin=open("input.txt", "rt")      

n, m = map(int, input().split())
arr = list(map(int,input().split()))

arr.sort()
count = 0

# p가 비어있으면 거짓, 비어있지 않으면 참을 출력
while arr:
  
    # 배열 값이 1개일 때 if 문에서 두번 더해지는 것을 방지하기 위한 if 문
    if len(arr) == 1:
        count += 1
        break
    
    if arr[0] + arr[-1] > m:
        arr.pop()
        count += 1
    else:
        arr.pop()
        arr.pop(0)
        count += 1

print(count)
