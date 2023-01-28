#BOJ10158개미
#점화식을 구하는게 문제의 핵심
#공간의 크기
w, h = map(int, input().split())
#좌표값 
p, q = map(int, input().split())
#개미가 움직일 시간 
t = int(input())

#증가인지 감소인지 확인
i = (p+t) // w 
j = (q+t) // h

#증가하면
if i % 2 == 0:
    result_i = (p+t) % w
#감소하면
else:
    result_i = w - (p+t) % w
    
#증가하면
if j % 2 == 0:
    result_j = (q+t) % h
#감소하면
else:    
    result_j = h - (q+t) % h
    
print(result_i, result_j)