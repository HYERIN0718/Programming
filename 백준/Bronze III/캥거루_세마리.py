a, b, c = map(int,input().split())
d = max(b-a, c-b)
print(d - 1)


# 내가 푼 답
'''
a, b, c = map(int,input().split())

if (b - a) < (c - b):
    print(c - b - 1)
else:
    print(b - a - 1)
'''    
    
