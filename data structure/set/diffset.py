# BOJ 1269: 대칭 차집합
import sys
input = sys.stdin.readline

n_A, n_B = map(int, input().split())

setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

diff1 = setA - setB
diff2 = setB - setA

print(len(diff1) + len(diff2))