# BOJ 1546: 평균
import sys
input = sys.stdin.readline

# N 입력
N = int(input().strip())

# 리스트 입력
num_list = list(map(int, input().split()))

# 최대값 추출
M = max(num_list)

# 새로운 점수 배열 정의
new_list = [num_list[i]/M*100 for i in range(N)]

# 평균 출력
print(sum(new_list)/N)