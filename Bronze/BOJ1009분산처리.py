#BOJ1009_분산처리
import sys
input = sys.stdin.readline

#입력
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    c = a % 10
    #상황에 따라 도출값 변경
    if c == 0:
        print(10)
    elif c in [1,5.6]:
        print(c)
        
    elif c in [4,9]:
        d = b % 2
        if d == 0:
            print(c*c%10)
        else:
            print(c)
            
    else:
        d = b % 4
        if d == 0:
            print(c**4%10)
        else:
            print(c**d%10)
    