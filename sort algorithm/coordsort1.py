# BOJ 11651: 좌표 정렬하기 2
import sys
input = sys.stdin.readline

N = int(input().strip())
coord = []
for _ in range(N):
    x, y = map(int, input().split())
    coord.append((x,y))
coord.sort(key=lambda x:(x[1], x[0]))

for c in coord:
    print(*c)