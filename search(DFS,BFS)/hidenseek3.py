# BOJ 13549: 숨바꼭질 3
# 디버그 함수 및 플래그 정의
import sys
from collections import deque
input = sys.stdin.readline
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
# N, K 입력
N, K = map(int, input().split())

# queue 선언
queue = deque()
queue.append((N, 0))

# visited 체크: 방문한 지점을 재방문하지 않게 하자
visited = [False] * 100001

# legal move 체크
# TODO: 파이썬은 자동 인라이닝 안된대서, 실전에서는 직접 적는게 좋은듯 ㅠㅠ
def check_legalmove(n):
    return 0 <= n <= 100000
    
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
    if check_legalmove(current_pos-1) and not visited[current_pos-1]:
        queue.append((current_pos-1, count+1))
    if check_legalmove(current_pos+1) and not visited[current_pos+1]:
        queue.append((current_pos+1, count+1))
    if check_legalmove(current_pos*2) and not visited[current_pos*2]:
        queue.appendleft((current_pos*2, count))