#BOJ3584_가장가까운공통조상_G4
#https://www.acmicpc.net/problem/3584 

# 20230916 복기
# 두 노드를 모두 자손으로 가지면서 깊이가 가장 깊은(즉 두 노드에 가장 가까운) 노드
# 두 노드가 주어질 때 공통된 조상들 중 가장 가까운 조상의 노드를 출력 

import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    tree = [0]*(n+1)
    #간선정보
    for _ in range(n-1):
        i, j = map(int, input().split())
        tree[j] = i
    # a가 b의 부모
    A, B = map(int, input().split())
    a_list, b_list = [0, A], [0, B]

    # 부모노드들을 저장해준다
    while tree[A]:
        a_list.append(tree[A])
        A = tree[A]
    while tree[B]:
        b_list.append(tree[B])
        B = tree[B]

    # -1 해주지 않으면 list 벗어남
    a_level=len(a_list)-1
    b_level=len(b_list)-1
                                        
    #부모노드가 같지 않을때까지 공통조상을 찾는다. 
    while a_list[a_level]==b_list[b_level]:   
        a_level-=1
        b_level-=1
 
    print(a_list[a_level+1])