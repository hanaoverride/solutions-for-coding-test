# BOJ 2292: 벌집
import sys
input = sys.stdin.readline

# 6방향 정의 - 계차수열
# 나머지 0: 5 11 17 (계차 6)
# 나머지 1: 6 12 18 (계차 6)
# 나머지 2: 1 7 13 (계차 6)
# 나머지 3: 2 8 14 (계차 6)
# 나머지 4: 3 9 15 (계차 6)
# 나머지 5: 4 10 16(계차 6)

# 계차수열 정의 at a = 6(0 is sentry)
diff = [0, 6]

# 찐 수열 정의
seq = [1]

N = int(input().strip())

if N == 1:
    print(1)
    exit()
    
while True:
    l = len(seq)
    if l > 1 and seq[-2] <= N <= seq[-1]:
        print(l)
        break
    next_seq = seq[-1] + diff[-1]
    next_diff = diff[-1] + 6
    seq.append(next_seq)
    diff.append(next_diff)