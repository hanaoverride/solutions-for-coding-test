# BOJ 18870: 좌표 압축
import sys
input = sys.stdin.readline

# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# 크기 순으로 정렬 후 인덱스 매핑
N = int(input().strip())

original_lst = list(map(int, input().split()))
tupled_lst = []
for i in range(N):
    tupled_lst.append((original_lst[i], i))
tupled_lst.sort(key=lambda x: x[0])

# "서로 다른" 좌표 갯수. 이 조건이 없다면 연속 조건을 사용하면 된다
coord = 0
prev = None # 주의: 값에 -1이 포함될 수 있어서 함부로 -1로 초기화하면 안됨 ㄷㄷ
compressed = [0]*N
for t in tupled_lst:
    val, idx = t
    if not prev == None and prev != val:
        coord += 1
    compressed[idx] = coord
    prev = val
    
print(*compressed)
    
    
    