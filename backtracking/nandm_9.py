# BOJ 15663: N과 M (9)
# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# N, M 입력
N, M = map(int, input().split())

# 숫자 리스트 생성
numberset = list(map(int,input().split()))

# numberset 정렬
numberset.sort()


# 결과를 저장할 집합 정의(중복 처리 하기 귀찮으니까 중복이 안되는 자료형 쓰자)
result = set()

# 탐색함수 search 정의
def search(curr_ptr, curr_depth, curr_list, visited):
    global result
    if curr_depth == M:
        result.add(tuple(curr_list))
        return
    for i in range(0, N):
        curr_list.append(numberset[i])
        if not visited[i]:
            visited[i] = True
            search(i, curr_depth + 1, curr_list, visited)
            visited[i] = False
        curr_list.pop()

# 탐색        
search(0, 0, [], [False]*N)
# set은 .sort가 아닌 sorted() 사용
for res in sorted(result):
    print(*res)