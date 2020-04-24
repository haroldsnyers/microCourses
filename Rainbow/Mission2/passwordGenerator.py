from passlib.hash import lmhash
import binascii, hashlib

username = ["aa", "ab", "bb", "aaa", "aab", "aba", "baa", "bab", "bba"]
passwords = ["xstv", "pomme", "poire", "peche", "fruit", "fuite", "fraise", "banane", "lemon"]

hashes = []
for password in passwords:
    hash = lmhash.hash(password)
    hashes.append(hash)

hashes1 = []
for password in passwords:
    hash = binascii.hexlify(hashlib.new('md4', password.encode('utf-16le')).digest())
    hashes1.append(hash)

file = open("LMhash.txt", "w")
for index in range(len(username)):
    file.write(str(username[index]) + ":" + str(hashes[index]) + "\n")
file.close()

file = open("NTLMhash.txt", "w")
for index in range(len(username)):
    file.write(str(username[index]) + ":" + str(hashes1[index])[2:34] + "\n")
file.close()
quit()
