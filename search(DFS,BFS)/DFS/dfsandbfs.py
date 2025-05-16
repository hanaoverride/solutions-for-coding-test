# BOJ 1260: DFS와 BFS
from collections import deque
# 디버그 함수 찾기
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# N, M, V 입력
N, M, V = map(int, input().split())

# N*N 인접행렬 생성(1-based index)
adj = [[False]*(N+1) for _ in range(N+1)]

# 간선 입력 및 연결(양방향)
for _ in range(M):
    start, end = map(int, input().split())
    adj[start][end] = adj[end][start] = True

# DFS 정의(stack 기반)
def DFS():
    visited = [False] * (N+1)
    stack = deque()
    stack.append(V)
    result = []
    while stack:
        current_node = stack.pop()
        if visited[current_node]:
            continue
        visited[current_node] = True
        result.append(current_node)
        # 각 노드 탐색(역순으로 탐색하니까 큰거부터 넣어야함)
        for i in range(N, 0, -1):
            if not visited[i] and adj[current_node][i]:
                stack.append(i)
    # 결과 출력
    print(*result)
    
# BFS 정의(queue 기반)
def BFS():
    visited = [False] * (N+1)
    queue = deque()
    queue.append(V)
    visited[V] = True
    result = []
    while queue:
        current_node = queue.popleft()
        result.append(current_node)
        # 각 노드 탐색(정방향 탐색하니까 작은거부터 넣어야함)
        for i in range(1, N+1):
            if not visited[i] and adj[current_node][i]:
                queue.append(i)
                visited[i] = True
    # 결과 출력
    print(*result)
    
# DFS, BFS 순서로 실행
DFS()
BFS()