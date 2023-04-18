#BOJ5588_별자리찾기_G4
m = int(input())
vc = [tuple(map(int, input().split())) for _ in range(m)]

n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]

print(vc)
print(p)
vc.sort()
p.sort()

startx, starty = vc[0]

for i in range(n):
    diffx = p[i][0] - startx
    diffy = p[i][1] - starty
    
    for j in range(m):
        vc[j] = (vc[j][0] + diffx, vc[j][1] + diffy)
        
    ans = 0
    for j in range(m):
        if vc[j] in p:
            ans += 1
            
    for j in range(m):
        vc[j] = (vc[j][0] - diffx, vc[j][1] - diffy)
        
    if ans == m:
        print(diffx, diffy)
        break
