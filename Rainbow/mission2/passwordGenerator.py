import csv
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
    print(hash)
    print(len(hash))
    print(str(hash)[2:34])


with open('text.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(zip(username, hashes))

# file1.close()  # to change file access modes


file = open("list.txt", "w")
for index in range(len(username)):
    file.write(str(username[index]) + ":" + str(hashes[index]) + "\n")
file.close()

file = open("list1.txt", "w")
for index in range(len(username)):
    file.write(str(username[index]) + ":" + str(hashes1[index])[2:34] + "\n")
file.close()
quit()
