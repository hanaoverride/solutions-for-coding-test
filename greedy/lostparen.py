# BOJ 1541: 잃어버린 괄호
# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# 문자열 입력
input_string = input()

# 그리디 전략: 뺄셈 다음에 괄호 안에 덧셈이 최대한 많이 연속되도록 더한다
# ex) -1 > - (1 + 2 + 3 + ...)
# 괄호 안에 숫자가 많이 들어갈수록 빼는 값이 커지므로 해가 최소가 됨이 보장된다.
# 한편 분배법칙에 의해 - (a + b + c + ...) = -a-b-c-...
# 따라서 한번 마이너스가 나왔다면 그 뒤의 부호를 전부 마이너스로 바꿔치기해도 해결이 된다.

# preprocessing
current_number = ""
new_list = []
minus_appeared = False
for char in input_string:
    if char == '+' or char == '-':
        if char == '-':
            minus_appeared = True
        new_list.append(int(current_number))
        if minus_appeared:
            new_list.append('-')
        else:
            new_list.append('+')
        current_number = ""
    else:
        current_number += char
new_list.append(int(current_number))

# 본격적으로 계산
result = new_list[0]
paren_list = []
for i in range(1, len(new_list), 2):
    if new_list[i] == '-':
        result -= new_list[i+1]
    elif new_list[i] == '+':
        result += new_list[i+1]
    
print(result)