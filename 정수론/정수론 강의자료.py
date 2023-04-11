# 1. 소수판정 : 1 주의
# 1과 자기자신 

# 2. 약수구하기 - 제곱수 주의 0(sqrtN)
n = int(input())
for i in range(1, int(n ** 0.5) + 1):
    if n % 1 == 0:
        print(i)
        if i * i != n:
            print(n // i)

# 3 소인수분해 >> 제곱수 주의 / 0(sqrtN)
n = int(input())
for i in range(2, n+1):
# for i in range(2, int(n ** 0.5) + 1):
    while n % i == 0:
        print(i)
        n //= i

# if n != 1:
#   print(n)


# 루트 n 보다 큰 값을 두 번 곱하면 n보다 크다
# 모든 소인수의 곱은 n이다
# 루트 n 보다 큰 소인수는 0개 혹은 1개다 

# 4 gcd lcm 
# a(더 큰 수 )와 b의 최대공약수는 b와 a-b의 약수다 
# gcd(a,b) 는 gcd(a % b, b)이다.

#유클리드 호제법
# 0(logN)
a, b = map(int, input().split())
while a % b != 0:
    a, b = b, a%b
print(b)

def get_gcd(a, b):
    while a % b != 0:
        a, b = b, a% b
    return b 

def get_lcm ( a, b):
    return a * b / get_gcd(a, b)

#에라토스테네스의 체 -> NlogN
#1. 모든 수가 소수다
#2. 1은 소수가 아니다 

n = int(input())
is_prime = [True for i in range(n+1)]
is_prime[i] = False

for i in range(2, n+1):
    if not is_prime[i]:
        continue
    for j in range(i*i, n+1, 1):
        is_prime[j] = True

#N//x = 1~N까지 X의 배수가 몇개있나?
#이건 팩토리얼을 위해 구하는 것!!

# N! 포함된 소수 X의 배수의 개수 구하기
# n! 포함된 x의 배수의 개수 => n // x*1 + n // x**2 ... log_x(n)

# nCm 오차없이 구하기 
# 26 * 8

# 연속된 k개의 수는 k의 배수가 존재한다.
# 30C15
# 한번씩 나눌때 나눠져서 연속된 숫자가 안되는거 아니냐?
# 2로 나눈 다음에 3의 배수가 나올 시점에 3의 사이클만큼 숫자가 더 나와서 가능하다. 

# 30 * 29 * 28 * 27 ... / 15 / 14 / 13 / 12 / ... / 1 
# 30 / 1 * 29 / 2 * 28 ...

# -> 코드로 나타내봐라 숙제 