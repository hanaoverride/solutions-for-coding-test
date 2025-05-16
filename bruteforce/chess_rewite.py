# BOJ 1018번: 체스판
# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# 내 생각에 최적해 배열을 미리 만들어놓고(어차피 두개밖에 없음 ㄷㄷ)
# 그 두개의 최적해 배열 중 최소 색칠 갯수가 나오는거 택하면 될거같음

# N, M 입력
N, M = map(int, input().split())

# 최적해 1,2 배열 생성
optimal1 = [[None]*M for _ in range(N)]
optimal2 = [[None]*M for _ in range(N)]

# 최적해 배열 채우기: 배열 1
for i in range(8):
    for j in range(8):
        optimal1[i][j] = 'W' if (i+j) % 2 == 0 else 'B'

# 최적해 배열 채우기: 배열 2
for i in range(8):
    for j in range(8):
        optimal2[i][j] = 'B' if (i+j) % 2 == 0 else 'W'
        
# 체스판 입력
chessboard = [input() for _ in range(N)]

debug(chessboard)
res1 = 9999999
# 해 계산: 배열 1을 8*8에 맞춰 슬라이딩 윈도우
for i in range(N-7):
    for j in range(M-7):
        case_res = 0
        for x in range(8):
            for y in range(8):
                case_res += optimal1[x][y] != chessboard[i+x][j+y]
        res1 = min(res1, case_res)

res2 = 9999999
# 해 계산: 배열 2 8*8에 맞춰 슬라이딩 윈도우
for i in range(N-7):
    for j in range(M-7):
        case_res = 0
        for x in range(8):
            for y in range(8):
                case_res += optimal2[x][y] != chessboard[i+x][j+y]
        res2 = min(res2, case_res)
        
# 최소값 출력
print(min(res1, res2))
