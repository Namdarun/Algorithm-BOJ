#BOJ14697_방배정_B2
#https://www.acmicpc.net/problem/14697
#방의 종류, 갯수와 상관없이 맞아떨어지는게 가능하다면 true

a, b ,c, total = map(int, input().split())
check = True
#a, b ,c 보는 범위를 몫에 제한하면 된다.
# 가능한 숫자 = 몫 // 에 * 값을 넣고 total이 가능하다면 0을 출력 
for i in range(total//a+1):
    for j in range(total//b+1):
        for k in range(total//c+1):
            if i*a + j*b + k*c == total:
                check = False

if check:
    print('0')

else:
    print('1')

