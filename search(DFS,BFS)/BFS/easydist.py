# BOJ 14940: 쉬운 최단거리

import sys
input = sys.stdin.readline
from collections import deque

DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
n, m = map(int, input().split())

inf = 10**10
dist = [[inf]*(m+1) for i in range(n+1)]
mmap = [0] + [[0] + list(map(int, input().split())) for i in range(n)]

# 시작 위치 탐색
def find_s(lst):
    for i in range(1, n+1):
        for j in range(1, m+1):
            if mmap[i][j] == 2:
                return (i, j)

start = find_s(mmap) + (0,)

# BFS 시작(x: x좌표, y: y좌표, d: 거리)
queue = deque([start])
tx, ty, td = start
dist[tx][ty] = td
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while queue:
    x, y, d = queue.popleft()
    debug(f"x,y,d: {x},{y},{d}")
    for dx, dy in directions:
        if 1 <= x + dx <= n and 1 <= y + dy <= m and dist[x+dx][y+dy] == inf and mmap[x+dx][y+dy] == 1:
            queue.append((x+dx, y+dy, d+1))
            dist[x+dx][y+dy] = d+1

for row in range(1, n+1):
    lst = []
    for item in range(1, m+1):
        if mmap[row][item] == 0:
            lst.append(0)
        elif dist[row][item] == inf:
            lst.append(-1)
        else:
            lst.append(dist[row][item])
    print(*lst)