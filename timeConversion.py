def timeConversion(s):
    lst=[]
    st=''
    t=s[8:]
    s=s[:8]
    lst=s.split(':')
    if t=='AM' and lst[0]=='12':
        lst[0]='00'
    elif t=='PM':
        if lst[0]=='12':
            lst[0]='12'
        else:
            temp=int(lst[0])+12
            lst[0]=str(temp)
    st=lst[0]+':'+lst[1]+':'+lst[2]
    return st

s = input()
result = timeConversion(s)
print(result)
