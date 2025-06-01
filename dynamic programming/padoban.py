# BOJ 9461: 파도반 수열

import sys
input = sys.stdin.readline

DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
T = int(input().strip())

# preprocess
P = [0]*101
P[1], P[2], P[3] = 1, 1, 1

for i in range(4, 101):
    P[i] = P[i-2] + P[i-3]

# solve for each case
for _ in range(T):
    geti = int(input().strip())
    print(P[geti])