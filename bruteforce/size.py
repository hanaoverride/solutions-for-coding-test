# BOJ 7568: 덩치
import sys
input = sys.stdin.readline

N = int(input().strip())

lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append((x, y))

result = []
for i in range(N):
    rank = 1
    x, y = lst[i]
    for j in range(N):
        if i == j:
            continue
        nx, ny = lst[j]
        rank += int(x < nx and y < ny)
    result.append(rank)

print(*result)