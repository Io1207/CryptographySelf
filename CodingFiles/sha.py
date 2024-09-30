import hashlib

def sha256String(input):
    sha256 = hashlib.sha256()
    
    sha256.update(input.encode('utf-8'))
    
    # Return the hexadecimal digest of the hash
    return sha256.hexdigest()

input = "Hello, this is my first time trying SHA hash for a string"
hash_value = sha256String(input)
print("SHA-256 Hash:", hash_value)