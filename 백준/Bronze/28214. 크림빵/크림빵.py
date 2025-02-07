N, K, P = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
ready = 0
for bread in range(N):
    check = 0
    for i in range(K):
        if arr[bread*K+i]==0:
            check+=1
    if check < P:
        ready += 1
    
print(ready)