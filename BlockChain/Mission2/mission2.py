import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
import binascii

keyPair = RSA.generate(2048)

pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})\n")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"\nPrivate key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})\n")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

msg = input("\nMessage to send : ").encode()
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print("\nEncrypted:", binascii.hexlify(encrypted))
h = SHA.new(msg)
signer = PKCS1_v1_5.new(keyPair)
signature = signer.sign(h)
print("Signature:", signature)

decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('\nDecrypted:', decrypted.decode())
h = SHA.new(decrypted)
verifier = PKCS1_v1_5.new(pubKey)
if verifier.verify(h, signature):
   print("The signature is authentic.")
else:
   print("The signature is not authentic.")
