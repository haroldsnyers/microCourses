from passlib.hash import lmhash
import binascii, hashlib

username = ["aa", "ab", "bb", "aaa", "aab", "aba", "baa", "bab", "bba"]
passwords = ["xstv", "pomme", "poire", "peche", "fruit", "fuite", "fraise", "banane", "lemon"]

hashes = []
for password in passwords:
    hash = lmhash.hash(password)
    hashes.append(hash)

file = open("LMhash.txt", "w")
for index in range(len(username)):
    file.write(str(hashes[index]) + "\n")
file.close()