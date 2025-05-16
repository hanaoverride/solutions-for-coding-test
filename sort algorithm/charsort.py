# BOJ 1181: 단어 정렬
# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        

# N 입력
N = int(input())

# 배열 생성
strings = []

# 문자열 입력
for i in range(N):
    new_str = input()
    # 중복 방지
    if not new_str in strings:
        strings.append(new_str)
    
# 정렬(람다식으로 길이값과 사전순을 넣어주자)
strings.sort(key=lambda x: (len(x), x))

# 출력
for string in strings:
    print(string)