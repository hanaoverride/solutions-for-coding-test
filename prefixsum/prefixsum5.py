# BOJ 11660: 구간 합 구하기 5
# 디버그 함수 및 플래그 정의
import sys
input = sys.stdin.readline
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# N, M 입력 
N, M = map(int, input().split())

# 표 입력
tile = [list(map(int, input().split())) for _ in range(N)]

# 정의된 1차원 구간합을 기반으로 2차원으로 확장
# 열방향 누적합 정의: row
row = [[0]*(N+1) for _ in range(N+1)]
# 1차원 구간합부터 먼저 정의
for i in range(1, N+1):
    for j in range(1, N+1):
        row[i][j] = row[i][j-1] + tile[i-1][j-1]

# 행방향 구간합 정의: col
col = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        col[i][j] = col[i-1][j] + row[i][j]

# 합 구하는 함수 제작: solve
def solve():
    # 좌표 입력
    x1, y1, x2, y2 = map(int, input().split())
    result = (
        col[x2][y2]
        - col[x1 - 1][y2]
        - col[x2][y1 - 1]
        + col[x1 - 1][y1 - 1]
    )
    print(result)
    
# solve를 M번 반복
for _ in range(M):
    solve()
