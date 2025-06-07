# BOJ 30804: 과일 탕후루
import sys
from itertools import combinations
input = sys.stdin.readline

DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
N = int(input().strip())

# B(9, 2) = 36 ~ max 7200000 iteration

fruits = list(map(int, input().split()))

if len(set(fruits)) <= 2:
    print(N)
    exit()

f_com = set(combinations(set(fruits), 2))

max_length = -1
for its in f_com:
    base_len = 0
    debug(*its)
    for i in range(N):
        if fruits[i] in its:
            base_len += 1
        else:
            base_len = 0
        max_length = max(max_length, base_len)
            
print(max_length)