import sys
sys.stdin=open("input.txt", "rt")

n = input()
s = 0
for i in n:
    if i.isdecimal():
        s = s * 10 + int(i)

# 내가 푼 답
''' n = list(map(str, str(input())))
a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
arr = []

for i in range(len(n)):
    if n[i] in a:
        arr.append(n[i])
arr = ''.join(arr)
s = int(arr)'''
    
print(s)

count = 0
for i in range(1, s + 1):
    if s % i == 0:
        count += 1
print(count)
