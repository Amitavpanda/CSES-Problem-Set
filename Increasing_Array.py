n = int(input())
x = list(map(int,input().split()))
ans = 0
for i in range(1,len(x)):
    if x[i] < x[i-1]:
        update = x[i-1] - x[i]
        x[i] += update
        ans += update
print(ans)