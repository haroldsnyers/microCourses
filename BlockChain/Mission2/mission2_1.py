import base64
import logging

from cryptography.exceptions import InvalidSignature
from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

# set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def exchange_safely_message(plain_text):
    """
    Example for cryptographic signing of a string in one method.
    - Generation of public and private RSA 4096 bit keypair
    - SHA-512 with RSA signature of text using PSS and MGF1 padding
    - BASE64 encoding as representation for the byte-arrays
    - UTF-8 encoding of Strings
    - Exception handling
    """
    try:
        # GENERATE NEW KEYPAIR
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096,
            backend=default_backend()
        )
        public_key = private_key.public_key()

        # ENCRYPTION
        cipher_text_bytes = public_key.encrypt(
            plaintext=plain_text.encode('utf-8'),
            # padding to obscure real message (many begin or end the same way)
            # mgf : mask generation function -> enables to have any output size
            # Optimal Asymmetric Encryption Padding (OAEP)
            padding=padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA512(),
                label=None
            )
        )

        # CONVERSION of raw bytes to BASE64 representation
        cipher_text = base64.urlsafe_b64encode(cipher_text_bytes)
        logger.info("Cypher_text : %s", cipher_text)

        # SIGN DATA/STRING
        signature = private_key.sign(
            data=plain_text.encode('utf-8'),
            # Probabilistic Signature Scheme
            padding=padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            algorithm=hashes.SHA256()

        )
        logger.info("Signature: %s", base64.urlsafe_b64encode(signature))

        # VERIFY JUST CREATED SIGNATURE USING PUBLIC KEY
        try:
            public_key.verify(
                signature=signature,
                data=plain_text.encode('utf-8'),
                padding=padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                algorithm=hashes.SHA256()
            )
            is_signature_correct = True
        except InvalidSignature:
            is_signature_correct = False

        logger.info("Signature is correct: %s", is_signature_correct)

        if is_signature_correct:
            # DECRYPTION
            decrypted_cipher_text_bytes = private_key.decrypt(
                ciphertext=base64.urlsafe_b64decode(cipher_text),
                padding=padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA512(),
                    label=None
                )
            )
            decrypted_cipher_text = decrypted_cipher_text_bytes.decode('utf-8')

            logger.info("Decrypted and original plain text are the same: %s",
                        decrypted_cipher_text == plain_text)
            logger.info("Decrypted message is : %s", decrypted_cipher_text)


    except UnsupportedAlgorithm:
        logger.exception("Signing failed")


if __name__ == '__main__':
    # demonstrate method
    exchange_safely_message(
        "Text that should be signed to prevent unknown tampering with its content.")
