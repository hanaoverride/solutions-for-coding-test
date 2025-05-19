# BOJ 2559: 수열

# 디버그 함수 생성
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
    
# N, K 입력
N, K = map(int, input().split())

# 온도 입력
temp = list(map(int, input().split()))

# 슬라이딩 윈도우: 초기 합을 길이 K의 윈도우 ~ [0, K)로 정의
sliding_window = sum(temp[:K])
# 최대 온도 정의. 초기값 = sum[0, K)
max_sum = sliding_window

# 슬라이딩 윈도우: [K, N) 구간에서 한칸씩 움직이자
for i in range(K, N):
    # 가장 앞에 있는 원소 제거 후 가장 뒷 원소를 더함
    sliding_window += temp[i] - temp[i-K]
    max_sum = max(max_sum, sliding_window)
    
# 결과값 출력
print(max_sum)