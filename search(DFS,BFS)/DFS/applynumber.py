# BOJ 2667번: 단지번호붙이기
from collections import deque
# 디버그 함수 찾기
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# N 입력
N = int(input())

# 지도 입력
apartment_map = [list(input()) for _ in range(N)]

# 순회 배열 생성
visited = [[False] * N for _ in range(N)]

# 방향 배열 생성
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 결과 배열 생성
result = []

debug(apartment_map)
# 순회 시작
for i in range(N):
    for j in range(N):
        if not visited[i][j] and apartment_map[i][j] == '1':
            # DFS 실행
            stack = deque()
            stack.append((i,j))
            count = 0
            while stack:
                current_pos = stack.pop()
                x, y = current_pos
                if visited[x][y]:
                    continue
                visited[x][y] = True
                count += 1
                for d in direction:
                    dx, dy = d
                    if 0 <= x + dx < N and 0 <= y + dy < N:
                        if not visited[x + dx][y + dy] and apartment_map[x + dx][y + dy] == '1':
                            stack.append((x + dx, y + dy))
            result.append(count)
            
# 결과값 오름차순 정렬
result.sort()

# 결과 출력
print(len(result))

# 각 경우의 수 출력
for r in result:
    print(r)