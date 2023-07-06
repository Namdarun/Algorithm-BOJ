#BOJ10994_별찍기19_S4
#https://www.acmicpc.net/problem/10994

#재귀로 풀려다가...노답이다 ㅠ

n = int(input())

#위
for i in range(n-1):
    print("* "*i + "*"*(1+4*(n-i-1)) + " *"*i)
    print("* "*(i+1) + " "*(1 + 4*(n-i-2)) + " *"*(i+1))
# 중간
print("* "*(2*n-1))
# 아래
for i in range(n-1):
    print("* "*(n-i-1) + " "*(1 + 4*i) + " *"*(n-i-1))
    print("* "*(n-i-2) + "*"*(1 + 4*(i+1)) + " *"*(n-i-2))
    