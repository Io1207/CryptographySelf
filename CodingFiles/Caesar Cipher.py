#Caesar Cipher

def encrypt(shift,text):
    encrypted=""
    for i in text:
        encrypted=encrypted+alphabets[(alphabets.index(text[i])+shift)%len(alphabets)]
    print (encrypted)

def decrypt(shift,text):
    decrypted=""
    for i in range(len(text)):
        decrypted=decrypted+ 0
    print(decrypted)

key=5
alphabets="abcdefghijklmnopqrstuvwxyz1234567890.* "
length=len(alphabets)
mode=int(input("Enter 0 for encrypt and 1 for decrypt"))
if mode!=1 and mode!=0:
    print("Invalid input")
    exit()
text=str(input("Enter the text please"))

if mode==0:
    encrypt(key,text)
else:
    decrypt(key,text)