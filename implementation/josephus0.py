# BOJ 11866: 요세푸스 문제
import sys
input = sys.stdin.readline

# N, K 입력
N, K = map(int, input().split())

# 테이블 정의: 다양한 방법이 있지만 여기선 리스트로(N=1000 정도에서...)
table = [i for i in range(1, N+1)]
# 요세푸스 순열 결과 저장
josephus = []
# killcount 저장. N명을 죽이면 끝납니다
killcount = 0
# 초기 포인터 선언. 원형 순회이므로 modular합니다.
curr_ptr = (K - 1) % N

# 요세푸스 시작
while killcount < N:
    # 포인터가 가리키는 사람을 처형
    josephus.append(table[curr_ptr])
    # 테이블에서 사람 제거 및 killcount 상승
    del table[curr_ptr]
    killcount += 1
    
    # 사람이 아직 다 죽지 않았다면, 다음 피처형인을 지정. K-1 move 뒤의 사람이 지정된다.
    if len(table) > 0:
        curr_ptr += K - 1
        curr_ptr %= len(table)
# 요세푸스가 끝났다면, 지정 형식에 맞추어 문자열 형성
result = "<"
for i in range(N):
    # 마지막 항이 아닌경우
    if i < N-1:
        result += f"{josephus[i]}, "
    else:
        result += f"{josephus[i]}>"
        
# 결과 출력
print(result)