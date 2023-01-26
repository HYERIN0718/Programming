n = int(input())
s = []
k = 0

for i in range(n):
    arr = list(map(int, input().split()))
    if arr[0] == arr[1] and arr[1] == arr[2]:
        s.append(10000 + arr[0]*1000)
    elif arr[0] == arr[1] :
        s.append(1000 + arr[0]*100)
    elif arr[1] == arr[2] :
        s.append(1000 + arr[1]*100)
    elif arr[0] == arr[2]:
        s.append(1000 + arr[2]*100)
    else:
        s.append(max(arr) * 100)
print(max(s)) 
