n = str(input())

for i in range(len(n) // 10 + 1):
    arr = ""
    arr += n[i*10:i*10 + 10]
    print(arr)
