from hashlib import sha256

message = input("Message to be hashed: ")
hash = sha256(message.encode())

print(hash)
