def compareTriplets(a, b):
    a1=0
    b1=0
    for i in range(len(a)):
        if a[i]>b[i]:
            a1=a1+1
        if a[i]<b[i]:
            b1=b1+1
    return a1,b1
a=[]
b=[]
for i in range(3):
    #for alice's score
    ele=int(input())
    a.append(ele)
for i in range(3):
    #for bob's score
    ele=int(input())
    b.append(ele)
result= compareTriplets(a,b)
print(result)
