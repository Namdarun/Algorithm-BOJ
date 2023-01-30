#BOJ14394_9-퍼즐
#https://www.acmicpc.net/problem/14394

import sys
input = sys.stdin.readline

arr = [[0]*26 for _ in range(2)]
for i in range(2):
#import sys때문에 rstrip을 받아야한다.
    for j in input().rstrip().replace('*','').lower():
        arr[i][ord(j)-97] += 1 
        
result = 0
for i in range(26):
    result += abs(arr[0][i]-arr[1][i])
    
print(result//2)
