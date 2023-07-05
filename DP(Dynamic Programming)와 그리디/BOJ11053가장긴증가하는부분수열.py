#BOJ11053_가장긴증가하는부분수열_S2
#https://www.acmicpc.net/problem/11053

#python3 - 31,256KB, 160ms
#pypy3 - 114,488KB, 128ms

#처음부터 차근차근, 배운 최장수열 알고리즘 적용
#input 
import sys
input = sys.stdin.readline

n = int(input())
#리스트에 담자
arr = list(map(int, input().split()))
#dp테이블 
lis = [1]*n

for i in range(1, n):
    for j in range(i):
        #이중반복문으로 최신화해나간다. 
        if arr[i] > arr[j]:
            lis[i] = max(lis[i], lis[j]+1)

print(max(lis))