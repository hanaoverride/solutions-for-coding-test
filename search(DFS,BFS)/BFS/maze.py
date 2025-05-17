# BOJ 2178: 미로 탐색
from collections import deque

# 디버그 함수 찾기
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# N, M 입력
N, M = map(int, input().split())

# 미로 배열 생성
maze = [list(input()) for _ in range(N)]

# 거리 배열 생성
dist = [[0]*M for _ in range(N)]

# 방향 배열 생성
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 최소거리 문제는 BFS가 최단경로를 보증함
# tuple = (x,y,dist)
queue = deque()
# 시작지점 (0,0,1)부터 시작
queue.append((0,0,1))
# 결과값 정의
result = 0
while queue:
    x, y, d = queue.popleft()
    if not dist[x][y] == 0:
        continue
    dist[x][y] = d
    for dx, dy in directions:
        if 0 <= x + dx < N and 0 <= y + dy < M:
            if dist[x + dx][y + dy] == 0 and maze[x + dx][y + dy] == '1':
                queue.append((x + dx, y + dy, d + 1))
debug(dist)
print(dist[N-1][M-1])
    