#BOJ11728_배열합치기_S5
#https://www.acmicpc.net/problem/11728
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
li_a = list(map(int, input().split()))
li_b = list(map(int, input().split()))
an = li_a + li_b
print(*sorted(an))