# import os
from passlib.hash import argon2
from argon2 import PasswordHasher

username = ["aa", "ab", "bb", "aaa", "aab", "aba", "baa", "bab", "bba"]
passwords = ["xstv", "pomme", "poire", "peche", "fruit", "fuite", "fraise", "banane", "lemon"]

hashes1 = []
ph = PasswordHasher()

for password in passwords:
    hash = ph.hash(password)
    print(hash)
    hashes1.append(hash)

file = open("hash.txt", "w")
for index in range(len(username)):
    file.write(str(username[index]) + ":" + str(hashes1[index]) + "\n")
file.close()

username = input("Enter username: ")
pwd = input("Enter password: ")

f = open("hash.txt", "r")
for line in f:
    user = line.split(":")
    if username == user[0]:
        hash = user[1]
        print(hash)
        try:
            print("Argon2 verify (incorrect password):", hash)
            print(ph.check_needs_rehash(hash))
            ph.verify(hash, pwd)
        except:
            print("Argon2 verify (incorrect password):", False)


