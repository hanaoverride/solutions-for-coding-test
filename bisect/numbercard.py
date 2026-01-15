# BOJ 10815: 숫자 카드
import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input().strip())
ref = list(map(int, input().split()))
M = int(input().strip())
valid = list(map(int, input().split()))

ref.sort()

res = []
for val in valid:
    find = bisect_left(ref, val)
    if find >= N:
        res.append(0)
    else:
        if ref[find] == val:
            res.append(1)
        else:
            res.append(0)

print(*res)