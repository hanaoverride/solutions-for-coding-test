# BOJ 1193: 분수찾기
import sys
from math import sqrt, ceil
input = sys.stdin.readline

X = int(input().strip())

# get groups: every group stacks a_n = n*(n+1)/2
# even number: from head
# odd number: from tail

# solve approx value of n*(n+1)/2 = X
# n*(n+1) = 2*X
# n^2 + n - 2*X = 0
# n = (-1+(1+8*X)**0.5)/2 (n>0)
# N ~ ceil(n)
n = int(ceil((-1+(1 + 8*X)**0.5)/2))

# set branch
start = -1
end = -1
diff = int(n*(n+1)/2 - X)

if n % 2 == 1:
    start = 1 + diff
    end = n - diff
else:
    start = n - diff
    end = 1 + diff

print(f"{start}/{end}")