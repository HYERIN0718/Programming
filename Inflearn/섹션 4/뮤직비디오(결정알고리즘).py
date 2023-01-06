import sys
#sys.stdin=open("input.txt", "rt")

# cd 개수 구하는 함수
def Count(c):

    # cd 개수
    count = 1

    # 최소 용량
    s = 0

    for x in arr:
        
        # 최소용량에 arr값을 더한 값이 mid값보다 클 때
        if s + x > c:
          
            # cd 값 1 증가
            count += 1
            
            # 최소 용량은 x로 초기화
            s = x
            
        # 그렇지 않을 때(mid값보다 작을 때)
        else:
            # 최소 용량에 arr값을 더함
            s += x
    return count

a, b = map(int, input().split())
arr = list(map(int, input().split()))

lt = 1
rt = sum(arr)
res = 0

while lt <= rt:
    mid = (lt+rt) // 2
    if Count(mid) <= b:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)
