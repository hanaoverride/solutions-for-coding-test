# BOJ 7576: 토마토
from collections import deque

# 디버그 함수 찾기
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# M, N 입력
M, N = map(int, input().split())

# 토마토 배열 생성
tomato = [list(map(int, input().split())) for _ in range(N)]

# ripeness 배열 생성(익을때까지 걸리는 날짜.)
ripeness = [[0]*M for _ in range(N)]

# direction 배열 생성(4방향)
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 모든 "1"(토마토 있음)을 큐에 넣고 동시에 BFS 시작(자연스럽게 익는 모습을 연상해요~)
# tuple = (xpos, ypos, day_count)
queue = deque()
for i in range(N):
    for j in range(M):
        # 토마토가 있는 각 칸을 큐에 삽입.
        if tomato[i][j] == 1:
            queue.append((i,j,1))
        # 토마토가 없는 칸은 미리 ripeness 처리
        if tomato[i][j] == -1:
            ripeness[i][j] = -1
# BFS 시작
result = -1
while queue:
    xpos, ypos, day_count = queue.popleft()
    if not ripeness[xpos][ypos] == 0:
        continue
    ripeness[xpos][ypos] = day_count
    result = max(result, day_count)
    # 4방향 탐색
    for dx, dy in direction:
        newx = xpos + dx
        newy = ypos + dy
        if 0 <= newx < N and 0 <= newy < M:
            # 토마토를 익히자
            if ripeness[newx][newy] == 0 and tomato[newx][newy] == 0:
                queue.append((newx, newy, day_count + 1))
                
# 탐색이 끝나고. ripeness = 0인 칸이 있는가? 즉 다 못익혔는가?
debug(ripeness)
flag = False
for i in range(N):
    if 0 in ripeness[i]:
        flag = True
        break

# 다 익었으면 결과값 출력.(0일부터 시작이니까 -1해줌.)
print(result - 1 if not flag else -1)