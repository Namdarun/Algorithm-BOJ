#BOJ1991_트리순회_S1
#https://www.acmicpc.net/problem/1991
#1학기에 했던 것 복습

import sys
input = sys.stdin.readline

N = int(input())
tree = {}
 
for n in range(N):
    #부모, 좌, 우노드
    root, left, right = map(str, input().split())
    tree[root] = [left, right]
 
 
#전위순회
def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right
 
#중위순회
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right
 
#후위순회 
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root
 
 
preorder('A')
print()
inorder('A')
print()
postorder('A')