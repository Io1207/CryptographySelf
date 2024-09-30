##AFFINE CIPHER

import numpy as np
a=int(input("Please enter a "))
b=int(input("Please enter b "))
#We know that each alphabet is represented by it's position in the 
#alphabet minus 1
#So I could create an array or I could make a dictionary
abc=np.array(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',' ','.'])
print(len(abc))
m=abc.size
preEncryption=np.zeros(m)
for i in range(m):
    preEncryption[i]=i
preEncryption=preEncryption.astype(int)
print(preEncryption)
postEncryption=np.zeros(m)
if a>m:
    x=a
else:
    x=m

exitStatus='No'
for i in range(2,(x//2)+1):
        #print("hello")
        if (a%i==0) and (m%i==0):
             print("Your key is invalid. Nice try!")
             exitStatus='Yes'
             break
        else:
             continue

if exitStatus!='Yes':
    postEncryption=(preEncryption*a+b)%m
    print(postEncryption)
    inputString=str(input("Please enter the input string "))
    inputString=inputString.lower()
    output=""
    for i in range(len(inputString)):
        inp=inputString[i]
    #print(inp)
        initial=int(np.where(abc==inp)[0][0])
        final=postEncryption[initial]
        output=output+abc[final]
    print(output)

print("thank you!")