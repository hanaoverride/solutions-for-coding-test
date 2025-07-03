# BOJ 1654: 랜선 자르기
import sys

input = sys.stdin.readline

K, N = map(int, input().split())

lst = []

for _ in range(K):
    newi = int(input().strip())
    lst.append(newi)
    
# define heuristic evaluation function
def h_eval(length, lines):
    return sum(line // length for line in lines)

lo = 1
hi = max(lst)
ans = 0
# take a binary search
while lo <= hi:
    mid = (lo + hi) // 2
    
    if h_eval(mid, lst) >= N:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)