import bcrypt
from argon2 import PasswordHasher
# set other environment for argon2

"""
    encryption password with bcrypt 
"""
salt = bcrypt.gensalt(rounds=16)
hash_bcrypt = bcrypt.hashpw("password".encode(), salt)

"""
    check password with bcrypts method 
    
    note : not working
"""
try:
    bcrypt.checkpw("pwd".encode(), hash_bcrypt)
    print("Bcrypt verify (incorrect password):", True)
except:
    print("Bcrypt verify (incorrect password):", False)

try:
    bcrypt.checkpw("password".encode(), hash_bcrypt)
    print("Bcrypt verify (incorrect password):", True)
except:
    print("Bcrypt verify (incorrect password):", False)

"""
    check password with by encrypting password again with salt  
"""
if bcrypt.hashpw("pwd".encode(), salt) == hash_bcrypt:
    print(True)
else:
    print(False)

if bcrypt.hashpw("password".encode(), salt) == hash_bcrypt:
    print(True)
else:
    print(False)

ph = PasswordHasher()
hash_argon2 = ph.hash("password")

"""
    check password with verify method of argon2  
"""
try:
    ph.verify(hash_argon2, "pwd")
    print("Argon2 verify (correct password):", True)
except:
    print("Argon2 verify (incorrect password):", False)

try:
    ph.verify(hash_argon2, "password")
    print("Argon2 verify (correct password):", True)
except:
    print("Argon2 verify (incorrect password):", False)