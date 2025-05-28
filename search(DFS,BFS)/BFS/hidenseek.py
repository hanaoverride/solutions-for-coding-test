# BOJ 1697: 숨바꼭질

import sys
from collections import deque
input = sys.stdin.readline

DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

N, K = map(int, input().split())


queue = deque()
queue.append((N, 0))

# visited 체크: 방문한 지점을 재방문하지 않게 하자
visited = [False] * 100001
    
# BFS 시작
while queue:
    current_pos, count = queue.popleft()
    debug(current_pos, count)
    
    if visited[current_pos]:
        continue
    visited[current_pos] = True
    
    if current_pos == K:
        print(count)
        break
    if 0 <= current_pos-1 <= 100000 and not visited[current_pos-1]:
        queue.append((current_pos-1, count+1))
    if 0 <= current_pos+1 <= 100000 and not visited[current_pos+1]:
        queue.append((current_pos+1, count+1))
    if 0 <= current_pos*2 <= 100000 and not visited[current_pos*2]:
        queue.appendleft((current_pos*2, count+1))