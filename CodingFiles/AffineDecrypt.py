import numpy as np
a=int(input("Please enter a "))
b=int(input("Please enter b "))
assert (a>0)
abc=np.array(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',' '])
print(len(abc))
m=abc.size
preDecryption=np.zeros(m)
for i in range(m):
    preDecryption[i]=i
preDecryption=preDecryption.astype(int)
print(preDecryption)
postDecryption=np.zeros(m)
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
inverse=a
for X in range(1,m+1):
    if (((a % m) * (X % m)) % m == 1):
        inverse=X
        break
# inverse=int(input("Enter the modular inverse of a"))
if exitStatus!='Yes':
    postDecryption=(inverse*(preDecryption-b))%m
    print(postDecryption)
    inputString=str(input("Please enter the input string "))
    inputString=inputString.lower()
    output=""
    for i in range(len(inputString)):
        inp=inputString[i]
    #print(inp)
        initial=int(np.where(abc==inp)[0][0])
        final=postDecryption[initial]
        output=output+abc[final]
    print(output)

print("thank you!")