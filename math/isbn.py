# BOJ 14626: ISBN
import sys
input = sys.stdin.readline

pos = None

isbn = list(input().strip())
mod = 0
# print(isbn)
for i in range(len(isbn)):
    if isbn[i] == '*':
        pos = i
    else:
        mod += int(isbn[i]) if i % 2 == 0 else 3*int(isbn[i])
        mod %= 10
if pos % 2 == 0:
    print((10 - mod) % 10)
# 3x + mod (mod 10) = 0
# 3x (mod 10) = 10 - mod
else:
    x = 0
    while True:
        if 3*x % 10 == (10 - mod) % 10:
            print(x)
            break
        x += 1