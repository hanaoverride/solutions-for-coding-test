# BOJ 1012: 유기농 배추
from collections import deque

# 디버그 함수 찾기
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# 문제 해결 함수 solve 정의
def solve():
    # M(가로길이), N(세로길이), K(좌표 갯수) 입력
    M, N, K = map(int, input().split())
    
    # 배추밭 배열 정의(0-based index)
    cabbage = [[0]*M for _ in range(N)]
    
    # 좌표 입력
    for _ in range(K):
        x, y = map(int, input().split())
        cabbage[y][x] = 1
    
    # visited 배열 정의
    visited = [[False]*M for _ in range(N)]
    
    # 방향 배열 directions 정의
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 결과값 변수 result 정의
    result = 0
    # 배추밭 순회
    for i in range(N):
        for j in range(M):
            # 아직 방문하지 않은 칸이면
            if not visited[i][j] and cabbage[i][j] == 1:
                stack = deque()
                stack.append((i,j))
                result += 1
                while stack:
                    current_pos = stack.pop()
                    x, y = current_pos
                    if visited[x][y]:
                        continue
                    visited[x][y] = True
                    for d in directions:
                        dx, dy = d
                        if 0 <= x + dx < N and 0 <= y + dy < M:
                            if not visited[x + dx][y + dy] and cabbage[x + dx][y + dy] == 1:
                                stack.append((x + dx, y + dy))
    # 결과 출력
    print(result)
                

# 테스트 케이스 T 입력
T = int(input())

# 테스트 케이스만큼 solve 반복
for _ in range(T):
    solve()
    