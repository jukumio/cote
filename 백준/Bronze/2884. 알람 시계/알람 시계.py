H, M = map(int, input().split())

if M >=45:
    M-=45
else:
    if H==0:
        H=23
    else: 
        H-=1
    
    M = M+60-45

print(H, M)