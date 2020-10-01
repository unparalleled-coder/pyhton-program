n=int(input())
lst=list(map(int,input().strip().split()))[:n]
z=max(lst)
while z==max(lst):
    lst.remove(max(lst))
print(max(lst))
