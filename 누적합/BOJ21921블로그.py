#BOJ21921_블로그_S3
#https://www.acmicpc.net/problem/21921

# 슬라이딩 윈도우 문제 

import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

hap = 0
prefix_hap =[0]
for i in arr:
    hap += i
    prefix_hap.append(hap)

result = []
count = 0
#슬라이딩 윈도우
while count + x <= n:
    result.append(prefix_hap[count+x]-prefix_hap[count])
    count += 1

# 계산값이 없을때
if max(result)==0:
    print('SAD')
else:
    print(max(result))
    print(result.count(max(result)))