import numpy as np

alphabets="abcdefghijklmnopqrstuvwxyz" #can be extended as per choice to include more characters like numbers and . and space and whatever you want
m=len(alphabets)
vigenere=np.zeros((m,m),dtype=str)
for row in range(m): #to initialise vigenere square matrix
    for column in range(m):
        vigenere[row][column]=alphabets[(row+column)%m]
#print(vigenere)
key=str(input("Please enter encryption key: "))
key=key.lower()
message=str(input("Please enter the string you wish to encrypt"))
message=message.lower()
n=len(message)
keyLen=len(key)
keyCircle=""
if keyLen<=n:
    for i in range(0,(n//keyLen)):
        keyCircle=keyCircle+key
    if n%keyLen!=0:
        for i in range(n%keyLen):
            keyCircle=keyCircle+key[i]
else:
    print("The length of your key exceeds the length of your message.")
    print("If you think this is not a mistake, continue otherwise please terminate this run")
    for i in range(n):
        keyCircle=keyCircle+key[i]
#print(keyCircle)

assert(len(keyCircle)==len(message))

#finding the substitute from vigenere
encryptedMessage=""
for i in range(len(message)):
    row=alphabets.find(message[i])
    column=alphabets.find(keyCircle[i])
    encryptedMessage=encryptedMessage+vigenere[row][column]
print(encryptedMessage)