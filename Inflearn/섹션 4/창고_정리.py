import sys
sys.stdin=open("input.txt", "rt")      

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

# 오름차순 정렬
arr.sort()

for _ in range(m):
    arr[0] += 1
    arr[n-1] -= 1
    
    # 가장 큰 값과 두 번째로 큰 값이 바뀔 수도 있기 때문에 sort()함수 반복
    arr.sort()
print(arr[n-1] - arr[0])
