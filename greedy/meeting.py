# BOJ 1931: 회의실 배정

# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# 회의 갯수 입력 (N <= 100000)
N = int(input())

# 회의시간 배열(tuple 입력. (start, end, time))
meeting_table = []

# 각 경우에 대해 입력
for _ in range(N):
    start, end = map(int, input().split())
    meeting_table.append((start, end))
    
meeting_table.sort(key=lambda x: (x[1], x[0]))

# 그리디 선택 기준: 일찍 끝나는것 중에서 가장 먼저 시작하는걸 연속해서 개최한다
# 이 방법이 최적해를 보증할 수 있음은 귀류법을 통해 증명 가능
debug(meeting_table)
result = 1
current_meeting = meeting_table[0]
for i in range(1, N):
    target_start, target_end = meeting_table[i]
    curr_start, curr_end = current_meeting
    if target_start >= curr_end:
        current_meeting = meeting_table[i]
        result += 1

# 결과 출력
print(result)
    
