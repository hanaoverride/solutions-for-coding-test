# BOJ 1074: Z

import sys
input = sys.stdin.readline

DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
N, r, c = map(int, input().split())

Zsol = {(1,1):1, (1,2):2, (2,1):3, (2,2):4}
def Z(size, x, y):
    debug(f"size, x, y: {size}, {x}, {y}")
    if size == 2:
        return Zsol[(x,y)]
    half = size // 2
    res = 0
    
    # left-top
    if x <= half and y <= half:
        debug("lt")
        res = Z(half, x, y)
    # right-top
    elif x <= half and y > half:
        debug("rt")
        res = half**2 + Z(half, x, y-half)
    # left-bottom
    elif x > half and y <= half:
        debug("lb")
        res = 2*half**2 + Z(half, x-half, y)
    # right-bottom
    else:
        debug("rb")
        res = 3*half**2 + Z(half, x-half, y-half)
    
    return res
    
print(Z(2**N,r+1,c+1)-1)
