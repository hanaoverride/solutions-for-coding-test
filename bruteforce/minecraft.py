# BOJ 18111: 마인크래프트

import sys
from collections import Counter
input = sys.stdin.readline

N, M, B = map(int, input().split())
minecraft = [list(map(int, input().split())) for _ in range(N)]

# N, M 범위가 작아서 최소~최대까지 비용 다 계산해도 무방할듯 ㅇㅇ;;
cost = 10**10
res_base = -1
minv = min(x for row in minecraft for x in row)
maxv = max(x for row in minecraft for x in row)

for base in range(minv, maxv+1):
    count = 0
    time = 0
    for i in range(N):
        for j in range(M):
            x = minecraft[i][j] - base
            count += x
            time += 2*x if x > 0 else -x
    if -count <= B and (time < cost or (time == cost and base > res_base)):
        cost = time
        res_base = base

print(cost, res_base)
