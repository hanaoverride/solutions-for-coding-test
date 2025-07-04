# BOJ 5525: IOIOI
import sys

input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
S = input().strip()
P = ['I' if x % 2 == 0 else 'O' for x in range(2*N+1)]

res = 0
ptr = 0
while ptr < M-1:
    if S[ptr] == 'O':
        ptr += 1
        continue
    count = 0
    while ptr+2 < M and S[ptr+1] == 'O' and S[ptr+2] == 'I':
        count += 1
        ptr += 2
        if count == N:
            res += 1
            count -= 1
    ptr += 1

print(res)