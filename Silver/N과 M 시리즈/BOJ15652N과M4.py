#BOJ15654_N과M4.py
#https://www.acmicpc.net/problem/15652

#BOJ15652_N과M (4)
n, m = map(int, input().split())
check = []
def suyeol(idx, count):
    if len(check) == m:
        # print(f'{map(str, check)}')
        for k in check:
            print(k, end=' ')
        print()
        return
        
    for i in range(idx, n+1): #for문 돌면서 숫자를 넣고, 
        check.append(i)       #스택이 비어있으면 바로 추가
        suyeol(i, count+1)    #재귀함수 
        check.pop()           #return되면 pop        
suyeol(1,0)

#백트래킹
#리스트 지우는 법 고민
#중복을 허용하게 된다.