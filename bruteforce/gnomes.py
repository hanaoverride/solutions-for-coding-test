# BOJ 2309: 일곱 난쟁이
import sys
from collections import deque
input = sys.stdin.readline

gnomes = [int(input().strip()) for x in range(9)]

gnomes.sort()

result = []
flag = False
visited = [False] * 10

# DFS
def DFS(depth, ptr, gnome_list):
    global flag
    if flag:
        return
    if depth == 7 or ptr == 9:
        # print(gnome_list)
        if sum(gnome_list) == 100:
            for c in gnome_list:
                print(c)
            flag = True
        return
    for i in range(ptr, 9):
        if not visited[i]:
            gnome_list.append(gnomes[i])
            visited[i] = True
            DFS(depth + 1, i, gnome_list)
            gnome_list.pop()
            visited[i] = False
DFS(0, 0, result)