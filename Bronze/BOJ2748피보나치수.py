#BOJ2748_피보나치수_B1
#https://www.acmicpc.net/problem/2748

n = int(input())

fibo =[0,1]
for i in range(2,n+1): 
    fibo.append(fibo[i-1]+fibo[i-2])
print(fibo[n])

#새로운 풀이 

n = int(input())

fibo =[0,1]
for i in range(2,n+1): 
    fibo.append(fibo[i-1]+fibo[i-2])
print(fibo[n])