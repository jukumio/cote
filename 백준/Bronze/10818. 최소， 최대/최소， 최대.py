N = int(input())
arr = list(map(int, input().split())) 
big = arr[0]
small = arr[0]
for i in arr[1:]:
    if i>big:
        big = i
    if i < small:
        small = i

print(small, big)