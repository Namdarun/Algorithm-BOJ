#BOJ2559_수열_S3
#https://www.acmicpc.net/problem/2559

#K개 구간의 온도합이 최대가 되는 그 값을 출력해라
#K까지 합을 설정해두고,
#K개씩 쪼갰을 때, 구간에 따른 합을 누적합과 비교해서 답을 도출한다.

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
suyeol = list(map(int, input().split()))

hap=check_hap=sum(suyeol[:k])

for i in range(k,n):
    hap = hap+suyeol[i]-suyeol[i-k]
    check_hap=max(hap, check_hap)

print(check_hap)