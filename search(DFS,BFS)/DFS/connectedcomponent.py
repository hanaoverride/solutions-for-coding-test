# BOJ 11724: 연결 요소의 개수
from collections import deque

# 디버그 함수 찾기
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# N, M 입력
N, M = map(int, input().split())

# 인접행렬 선언
adj = [[False] * (N + 1) for _ in range(N + 1)]

# M개의 간선 입력(무방향)
for _ in range(M):
    x, y = map(int, input().split())
    adj[x][y] = adj[y][x] = True

# visited 행렬 선언
visited = [False] * (N+1)

# 결과 변수 result 선언
result = 0

# 각 노드에서 탐색 시작
for i in range(1, N+1):
    if not visited[i]:
        # DFS 시작
        stack = deque()
        stack.append(i)
        result += 1
        while stack:
            current_node = stack.pop()
            if visited[current_node]:
                continue
            visited[current_node] = True
            for i in range(1, N+1):
                if not visited[i] and adj[current_node][i]:
                    stack.append(i)

# 결과값 출력
print(result)
