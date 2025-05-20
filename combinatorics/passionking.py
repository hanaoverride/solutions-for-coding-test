# BOJ 9375: 패션왕 신해빈
from itertools import combinations
# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# 테스트 케이스 T 입력
T = int(input())

# 문제 해결 함수 solve 선언
def solve():
    # 패션 가짓수 N 입력
    N = int(input())
    
    # 카테고리 count dict 선언
    category_count = dict()
    
    # 옷 조합 입력
    for _ in range(N):
        # 이름과 종류 입력
        name, category = map(str, input().split())
    
        # 카테고리 카운팅
        if category in category_count:
            category_count[category] += 1
        else:
            category_count[category] = 1
            
    # 곱의 법칙 사용(안입음, 1개 입음, 2개 입음, ... , n개 입음 = n+1가지)
    result = 1
    for k, v in category_count.items():
        result *= (v + 1)
    
    # 아무것도 선택하지 않는 공집합 제외
    print(result - 1)
# 테스트케이스 T번 solve()
for _ in range(T):
    solve()
    
    