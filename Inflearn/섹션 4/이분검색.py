import sys
sys.stdin=open("input.txt", "rt")


### 내가 푼 답
a, b = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
n = 0

for i in range(a):
    if arr[i] == b:
        n = i + 1   
print(n)


### 이분검색으로 푼 정답
a, b = map(int, input().split())
arr = list(map(int, input().split()))
lt = 0
rt = a - 1
arr.sort()

# lt가 rt보다 커지면 반복문 종료
while lt <= rt:
    mid = (lt+rt) // 2
    if arr[mid] == b:
        print(mid + 1)
        break
    elif arr[mid] > b:
        rt = mid - 1
    else:
        lt = mid + 1
