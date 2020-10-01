num = int(input('Enter the number:'))
sum=0
temp=num
i=2
while temp>0:
    rem=temp%10
    sum=sum*10+rem
    temp=temp//10

if sum==num:
    print(num,'is palindrome number')
else :
    print(num,'is not palindrome number')
