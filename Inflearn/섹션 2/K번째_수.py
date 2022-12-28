import sys
#sys.stdin=open("input.txt", "rt")

T = int(input())

for t in range(1, T + 1):
    n, s, e, k= map(int, input().split())
    arr_list = list(map(int, input().split()))
    arr_list = arr_list[s-1:e]
    arr_list.sort()

    print("#%d %d" %(t, arr_list[k - 1]))
