#BOJ2805_나무자르기_S2
#https://www.acmicpc.net/problem/2805

#함수로 만들어서 풀어보자

#BOJ13702_이상한술집_S3
#https://www.acmicpc.net/problem/13702

import sys
input = sys.stdin.readline

def binary(arr_input, s, e):
    ans = 0 
    while (s <= e):
        mid = (s + e) // 2
        cnt = 0 

        for i in arr_input:
            if i > mid:
                cnt = i - mid

        if cnt >= m:
            ans = mid
            s = mid + 1

        else: 
            e = mid - 1

    #답을 리턴해주자
    return ans

n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = binary(arr, 0, max(arr))
print(result)



