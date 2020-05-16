import hashlib


class Block:
    def __init__(self, content, difficulty=1):
        self._content = content
        self._nonce = 0
        self._hash = None
        self.difficulty = difficulty
        self.algo_nonce()

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
        return self._hash

    def __str__(self):
        return '=== Block ===\nContent: {}\nNonce  : {}\nHash   : {}'.format(self._content, self._nonce, self._hash)

    def algo_nonce(self):
        nonce = 0
        while not self._update_hash().startswith('0' * self.difficulty):
            nonce += 1
            self._nonce = nonce
            self._update_hash()


if __name__ == '__main__':
    a = Block('Foo')
    print(a)

    a = Block('Foo', 2)
    print(a)

    a = Block('Foo', 3)
    print(a)

    a = Block('Foo', 4)
    print(a)
