# BOJ 1764: 듣보잡
import sys
input = sys.stdin.readline

# N, M 입력
N, M = map(int, input().split())

# 듣도 못한 사람
not_heard = set()

for _ in range(N):
    person = input().strip()
    not_heard.add(person)

# 보도 못한 사람
not_seen = set()

for _ in range(M):
    person = input().strip()
    not_seen.add(person)

# 듣도 보도 못한사람 출력
not_known = sorted(not_heard & not_seen)
print(len(not_known))
for member in not_known:
    print(member)