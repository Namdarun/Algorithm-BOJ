#BOJ1408_24_B2
#https://www.acmicpc.net/problem/1408

#구현
t1 = list(map(int, input().split(':')))
t2 = list(map(int, input().split(':')))
t1_sec = t1[0]*3600 + t1[1]*60 + t1[2]
t2_sec = t2[0]*3600 + t2[1]*60 + t2[2]
result = t2_sec - t1_sec

if result < 0:
    result += 24*3600

print(f'{result//3600:02d}:{(result%3600)//60:02d}:{result%60:02d}')