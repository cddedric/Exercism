import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    h=0
    if s[-2]=='A' and s[0:2]=='12':
        s='00'+s[2:]
    if s[-2]=='P':
        h=int(s[0:2])+12
        if h>=24:
            h-=24
            s='0'+str(h)+s[2:-2]
        else:
            s=str(h)+s[2:-2]
    else:
        s=s[0:-2]
    return s

      
n= 133

if n<124:
    print("123")
else:
    out=''
    for i in range(123,n):
        out+=str(i)+' '
    print(out+str(n))