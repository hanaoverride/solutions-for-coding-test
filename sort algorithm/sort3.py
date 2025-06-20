# BOJ 10989: 수 정렬
# use counting sort
import sys
input = sys.stdin.readline

N = int(input().strip())
# N <= 10000
count = [0] * 10001

for _ in range(N):
    item = int(input().strip())
    count[item] += 1
    
for i in range(1, 10001):
    for j in range(count[i]):
        print(i)