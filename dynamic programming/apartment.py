# BOJ 2775: 부녀회장이 될테야
import sys
input = sys.stdin.readline

T = int(input().strip())

apartment = [[0]*15 for _ in range(15)]

apartment[0] = [i for i in range(15)]

# preprocess
for i in range(1, 15):
    for j in range(15):
        # can be improved by prefix sum.
        apartment[i][j] = sum(apartment[i-1][:(j+1)])
    # print(apartment[i])

def solve():
    k = int(input().strip())
    n = int(input().strip())
    
    print(apartment[k][n])

# now do stuff
for _ in range(T):
    solve()
    
    