# BOJ 1991: 트리 순회
# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# N 입력
N = int(input())
        
# 노드 클래스 정의
class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
# 알파벳 정의
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# 노드 정의
nodes = dict()

for i in range(N):
    nodes[alphabet[i]] = Node(alphabet[i])

# 연결 입력
for _ in range(N):
    rt, l, r = map(str, input().split())
    if l != '.':
        nodes[rt].left = nodes[l]
    if r != '.':
        nodes[rt].right = nodes[r]

# 전위, 중위, 후위순회 함수 정의
res1 = ""
def preorder(node):
    global res1
    # node - left - right
    res1 += node.item
    if node.left != None:
        preorder(node.left)
    if node.right != None:
        preorder(node.right)
res2 = ""
def inorder(node):
    global res2
    # left - node - right
    if node.left != None:
        inorder(node.left)
    res2 += node.item
    if node.right != None:
        inorder(node.right)
res3 = ""
def postorder(node):
    global res3
    # left - right - node
    if node.left != None:
        postorder(node.left)
    if node.right != None:
        postorder(node.right)
    res3 += node.item

# 각각 순회
preorder(nodes['A'])
inorder(nodes['A'])
postorder(nodes['A'])

print(res1)
print(res2)
print(res3)