# BOJ 9663: N-Queen
# 디버그 함수 찾기
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# N 입력
N = int(input())

# 룩 가로세로 갯수는 N
rook_check_vertical = [False]*(N+1)
rook_check_horizontal = [False]*(N+1)
# 비숍 대각선의 갯수는 2N
bishop_check_rightupper = [False]*(2*N+1)
bishop_check_leftupper = [False]*(2*N+1)

# 결과값
result = 0
# 퀸의 행마법은 룩 + 비숍이다.
def NQueen(current_queen_count, r1, r2, b1, b2):
    global result
    # 모든 퀸을 성공적으로 배치
    if current_queen_count == N+1:
        result += 1
    # 내 생각에 각 직선, 대각선에 대해 check 배열을 만들어서 넘기는게 나을듯??
    for i in range(1, N+1):
        # 룩 행마법과 비숍 행마법 동시 계산
        if not r1[i] and not r2[i] and not b1[current_queen_count + i] and not b2[current_queen_count - i + N]:
            # 체크인
            r1[i], r2[i] = True, True
            b1[current_queen_count + i], b2[current_queen_count - i + N] = True, True
            # 순회
            NQueen(current_queen_count+1, r1, r2, b1, b2)
            # 체크아웃
            r1[i], r2[i] = False, False
            b1[current_queen_count + i], b2[current_queen_count - i + N] = False, False
# NQueen 실행
NQueen(1, rook_check_horizontal, rook_check_vertical, bishop_check_leftupper, bishop_check_rightupper)
print(result)
    
                
            
    