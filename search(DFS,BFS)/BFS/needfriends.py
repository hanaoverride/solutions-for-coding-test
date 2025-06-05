# BOJ 21736: 헌내기는 친구가 필요해
import sys
from collections import deque
input = sys.stdin.readline

DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
N, M = map(int, input().split())

campus = [list(input().strip()) for _ in range(N)]

def getStartPos(lst):
    debug(lst)
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 'I':
                return (i, j)
    # default
    return (0, 0)

queue = deque([getStartPos(campus)])
res = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False]*M for _ in range(N)]

while queue:
    x, y = queue.popleft()
    if visited[x][y]:
        continue
    visited[x][y] = True
    res += int(campus[x][y] == 'P')
    debug(f"x, y: {x}, {y}")
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and campus[nx][ny] != 'X':
            queue.append((nx, ny))

print(res if res != 0 else 'TT')