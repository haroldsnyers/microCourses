import hashlib

class Block:
    def __init__(self, content):
        self._content = content
        self._nonce = 0
        self._hash = None
        self._update_hash()

    @property
    def nonce(self):
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        self._nonce = nonce
        self._update_hash()

    def _update_hash(self):
        msg = hashlib.sha512()
        msg.update('{}{}'.format(self._content, self._nonce).encode())
        self._hash = msg.hexdigest()

    def __str__(self):
        return '=== Block ===\nContent: {}\nNonce  : {}\nHash   : {}'.format(self._content, self._nonce, self._hash)


if __name__ == '__main__':
    a = Block('Foo')
    print(a)