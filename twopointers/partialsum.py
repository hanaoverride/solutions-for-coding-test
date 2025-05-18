# BOJ 1806번: 부분합

# 디버그 함수 생성
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# N, S 입력
N, S = map(int, input().split())

# 수열 입력
seq = list(map(int, input().split()))

# 투 포인터 설정 : pt_start, pt_end(0-based index)
pt_start, pt_end = 0, 0

# 현재 합 정의
curr_sum = 0

# 최소 구간 길이 정의
min_length = 9999999

# 투 포인터 루프 시작
while True:
    # case 1: 합이 여전히 목표치 S보다 작다
    if curr_sum >= S:
        # 최소 구간 갱신
        min_length = min(min_length, pt_end - pt_start)
        curr_sum -= seq[pt_start]
        pt_start += 1
    # 끝 포인터가 수열을 벗어났을 경우: break
    elif pt_end >= N:
        break
    # case 2: 합이 목표치 S 이상이다
    else:
        curr_sum += seq[pt_end]
        pt_end += 1
    
    debug(f"curr_sum, pt_start, pt_end: {curr_sum}, {pt_start}, {pt_end}")
    
# 결과값 출력
print(min_length if not min_length == 9999999 else 0)