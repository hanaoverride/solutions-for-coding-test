# BOJ 2630: 색종이 만들기
import sys
input = sys.stdin.readline

# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# N 입력
N = int(input().strip())

# 색종이 입력
paper = [list(map(int, input().split())) for _ in range(N)]

# 카운터 정의(0, 1)
counter = [0] * 2
# 분할정복 재귀 정의(x, y는 top-left 좌표)
def recursion(size, x, y):
    s = 0
    for i in range(size):
        s += sum(paper[x+i-1][y-1:y+size-1])
    debug(f"s: {s}")
    # 값이 0 혹은 1밖에 없으므로 identical 하면 합의 결과는 0 혹은 size^2밖에 나오지 않는다.
    if s % (size ** 2) == 0:
        counter[paper[x-1][y-1]] += 1
        return
    
    # 격자는 현재 N의 절반
    grid = size // 2
    
    # 4분할 정복 시작
    # top-left
    recursion(grid, x, y)
    # top-right
    recursion(grid, x + grid, y)
    # bottom-left
    recursion(grid, x, y + grid)
    # bottom-right
    recursion(grid, x + grid, y + grid)
    
# 재귀호출
recursion(N, 1, 1)

# 결과 출력
print(*counter, sep='\n')