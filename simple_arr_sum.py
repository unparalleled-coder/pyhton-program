n=int(input())
arr=[]
sum=0
for i in range(n):
    ele=int(input())
    arr.append(ele)
for i in range(len(arr)):
    sum=sum+arr[i]
print(sum)
