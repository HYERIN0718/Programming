import sys
sys.stdin=open("input.txt", "rt")

# Count(x) - 표준 랜선 개수 카운팅
# len - 자르려는 랜선 길이
# cnt - 랜선 총 개수
def Count(len):
    cnt = 0
    for x in arr:
        cnt += (x // len)
    return cnt

a, b = map(int, input().split())
arr = []
res = 0 # 최종 길이
largest = 0 # 갖고있는 랜선의 최대 길이

for i in range(a):
    n = int(input())
    
    # 갖고 있는 랜선을 배열에 넣음
    arr.append(n)
    
    # 랜선 중에서 가장 큰 값을 largest에 넣음
    largest = max(largest, n)

lt = 1
rt = largest

while lt <= rt:
    mid = (lt+rt) // 2
    
    # b(원하는 랜선 개수)보다 커도 상관없기 때문에 lt를 늘려서 최대 랜선 길이를 구함
    if Count(mid) >= b:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1 
print(res)
