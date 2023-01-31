## 전위순회
def DFS(v):
    if v > 7:
        return
    else:
        # 출력 => 순회방문
        # print()작업을 한 후에 왼쪽노드와 오른쪽노드 처
        print(v, end=' ') 
        
        DFS(v * 2)
        DFS(v * 2 + 1)

if __name__=="__main__":
    DFS(1)
    
    
    
## 중위순회
def DFS(v):
    if v > 7:
        return
    else:        
        DFS(v * 2)
        
        # 왼쪽노드가 먼저 처리하고 print()작업 진행한 후에 오른쪽 노드 처리
        print(v, end=' ')
        
        DFS(v * 2 + 1)

if __name__=="__main__":
    DFS(1)
    
    
    
## 후위순회
def DFS(v):
    if v > 7:
        return
    else:        
        DFS(v * 2)
        DFS(v * 2 + 1)
        
        # 왼쪽노드와 오른쪽노드를 먼저 처리한 후에 print()작업
        print(v, end=' ')

if __name__=="__main__":
    DFS(1)
    
    
