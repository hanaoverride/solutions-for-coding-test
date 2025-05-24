# BOJ 30802: 웰컴 키트
# 아니 이거 국어문제 아님???
import sys
from math import ceil
input = sys.stdin.readline

# N 입력
N = int(input().strip())

# 사이즈 입력
S, M, L, XL, XXL, XXXL = map(int, input().split())

# T, P 입력
T, P = map(int, input().split())

# 티셔츠는 남아도 되지만 부족하면 안된다. ~ 인원수 최대에 맞춰 분할 후 올림
shirts_count = 0
shirts_count += int(ceil(S/T))
shirts_count += int(ceil(M/T))
shirts_count += int(ceil(L/T))
shirts_count += int(ceil(XL/T))
shirts_count += int(ceil(XXL/T))
shirts_count += int(ceil(XXXL/T))

print(shirts_count)

# 펜 분배: 몫, 나머지
print(N//P, N%P)