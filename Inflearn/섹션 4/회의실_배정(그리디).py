import sys
sys.stdin=open("input.txt", "rt")      

# 내가 푼 답(a배열만 혼자 만들었음)
'''n = int(input())
a = []

for i in range(n):
    arr = list(map(int, input().split()))
    a.append(arr) 
a.sort(key = lambda x: [x[1], x[0]])

count = 0
et = 0

for s, e in a:
    if s >= et:
        et = e
        count += 1

print(count)
'''

# 정답
import sys
sys.stdin=open("input.txt", "rt")      

n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
                    
                    # (s, e) : 튜플 형태로 생성
    meeting.append((s, e))
    
# 회의가 끝나는 시간을 기준으로 오름차순 정렬
# 리스트.sort(key=lambda x) : key는 sort 정렬 기준
meeting.sort(key=lambda x : (x[1], x[0]))

et = 0 # 회의가 끝나는 시간 
count = 0
for s, e in meeting:
    if s >= et:
        et = e
        count += 1
print(count)


