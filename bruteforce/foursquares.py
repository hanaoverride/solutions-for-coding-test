# BOJ 17626: Four Squares

import sys
from collections import deque
from math import isqrt
input = sys.stdin.readline

DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        

n = int(input().strip())

# BFS
# def: (remaining, dim)
queue = deque([(n, 1)])
visited = set()
visited.add(n)

while queue:
    remaining, dim = queue.popleft()
    sqrt_r = isqrt(remaining)
    if sqrt_r ** 2 == remaining:
        print(dim)
        break
    # 제출된 코드에서 개선: edge case 처리
    if dim > 4:
        continue
    i = 1
    while i*i<=remaining:
        nxt = remaining-i**2
        if nxt not in visited:
            queue.append((nxt, dim+1))
            visited.add(nxt)
        i += 1