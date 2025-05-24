# BOJ 10816: 숫자카드 2
import sys
input = sys.stdin.readline

# N 입력
N = int(input().strip())

# 카드 목록 입력
card = list(map(int, input().split()))

# 딕셔너리 선언 후 카드 갯수 카운팅(음수도 있어서 이렇게 해야함)
card_count = dict()

for c in card:
    if not c in card_count:
        card_count[c] = 1
    else:
        card_count[c] += 1

# 구해야 할 갯수 M 입력
M = int(input().strip())

# 인덱스 목록 입력
index = list(map(int, input().split()))

# 결과를 담을 result 리스트 추가
result = []

# 딕셔너리 접근 루프
for i in index:
    result.append(card_count[i] if i in card_count else 0)
    
# 결과를 unzip해서 출력
print(*result)