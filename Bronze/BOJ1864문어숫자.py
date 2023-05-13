#BOJ1864_문어숫자_B2
#https://www.acmicpc.net/problem/1864

#단순 구현

d = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}
while 1:
    s = input()
    if s == '#':
        break
    res = 0
    for i in range(len(s)):
        res += d[s[i]] * 8**(len(s)-i-1)
    print(res)