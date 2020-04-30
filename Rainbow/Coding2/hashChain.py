import hashlib
import string
import random


class HashChain:
    def __init__(self, size=8, password_length=8, number_of_passwords=10):
        self.hash_chain = []
        self.passwords_covered = []
        self.hashes_covered = []
        self.passwords = []
        self.size = size
        self.characters = string.ascii_lowercase + string.digits
        self.characters_list = [i for i in self.characters]
        self.password_length = password_length
        self.number_of_passwords = number_of_passwords

    def password_generator(self):
        """
        :return: string of random
        """
        return ''.join(random.choice(self.characters) for _ in range(self.password_length))

    def generates_list_words(self):
        """
            generates a list (nop duplicates) of password of a given size
        """
        while len(self.passwords) < self.number_of_passwords:
            word = self.password_generator()
            if word not in self.passwords:
                self.passwords += word

    def hash(self, password):
        """

        :param password: password to hash
        :return: returns hashed password (sha256)
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def reduce(self, int_, index):
        """
        reduction method to come to a password from a hash given column position
        :param int_: int of hash to reduce
        :param index: column of table and thus changes reduction
        :return: reduced password from given hash and column
        """
        pwd = ""
        while len(pwd) < self.password_length:
            pwd = pwd + self.characters_list[(index + int_) % len(self.characters)]
            int_ = int_ // len(self.characters)
        return pwd

    def generate_chain(self, password):
        """
        generates a chain of given length (size) starting from a given password
        appends all the hashes and passwords covered to given lists for further purposes
        :param password: password from which to begin chain
        """
        a = password
        hash_chain_temp = [a]
        self.passwords_covered.append(password)
        for x in range(self.size):
            hash = self.hash(a)
            a = self.reduce(int(hash, 16), x)
            hash_chain_temp.append(hash)
            hash_chain_temp.append(a)
            self.passwords_covered.append(a)
            self.hashes_covered.append(hash)
        hash = self.hash(a)
        hash_chain_temp.append(hash)
        self.hashes_covered.append(hash)
        print(hash_chain_temp)
        self.hash_chain.append(hash_chain_temp)

    def create_table(self):
        """creates table with the whole chains"""
        self.generates_list_words()
        for password in self.passwords:
            self.generate_chain(password)

    def check_collisions(self):
        """
            Checks if there are any collisions, thus duplicates in all the passwords covered
            A set is an unordered collection of items. Every element is unique
            (no duplicates) and must be immutable (which cannot be changed).
        """
        print("This table contains collisions : " + str((len(self.hashes_covered) != len(set(self.hashes_covered)))))


hash_chain = HashChain()
hash_chain.create_table()
hash_chain.check_collisions()
