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

    def sum_numbers_hash(self):
        result = 0
        for item in self._update_hash():
            try: 
                result += int(item)
            except: 
                pass
        return result

    def count_occurrences(self):
        dico = {}
        for elem in self._update_hash():
            try:
                dico[elem] += 1
            except:
                dico[elem] = 1
        value_max = 0
        for key in dico:
            if dico[key] > value_max:
                value_max = int(dico[key])

        return value_max

    def algo_nonce(self):
        nonce = 0  
        while (
            not self._update_hash().startswith('0' * self.difficulty)
            ) or (
                self.sum_numbers_hash() % self.difficulty
            ) or (
                self.count_occurrences() < self.difficulty + 14):
            # (x % y) is the same as (x % y != 0)
            nonce += 1
            self._nonce = nonce

if __name__ == '__main__':
    a = Block('Foo')
    print(a)

    a = Block('Foo', 2)
    print(a)

    a = Block('Foo', 3)
    print(a)

    a = Block('Foo', 4)
    print(a)
