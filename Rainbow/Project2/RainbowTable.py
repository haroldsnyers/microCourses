from passlib.hash import lmhash
import hashlib
import string
import random
import json
import os


class RainbowGenerator:
    def __init__(self, columns=0, rows=10, list_passwords=None, hash_type="lmhash", password_max_len=7):
        self.columns = columns
        self.rows = rows
        self.hash_type = hash_type
        self.password_max_size = password_max_len
        self.chars = string.ascii_lowercase + string.digits
        self.rain_table = []
        self.word_table = []
        self.hash_table = []
        self.collisions = 0
        self.password_tested = 0
        self.success_ratio = 0
        if self.recover_rainbow_table() is False:
            print("# " + "Creating a new RainbowTable")
            if list_passwords is None:
                self.passwords = self.generates_list_words()
            else:
                self.passwords = list_passwords
            self.build_table()
            self.test_collisions()
            self.test_rain()
            self.write_to_file()
        else:
            print("# " + "Recovering the RainbowTable")
            print("Number of passwords covered with this table : " + str(self.password_tested))
            print("Success rate of this table is : " + str(self.success_ratio) + "%")

    def password_generator(self):
        return ''.join(random.choice(self.chars) for _ in range(self.password_max_size))

    def generates_list_words(self):
        """
            generates a list (nop duplicates) of password of a given size
            :returns password list to generate rainbow table from
        """
        while len(self.passwords) < self.rows:
            word = self.password_generator()
            if word not in self.passwords:
                self.passwords += word
        return self.passwords

    def hash_word(self, word):
        """
        word: word to hash
        Returns the hashed word
        """
        hash = None
        if self.hash_type == "lmhash":
            hash = lmhash.hash(word)
        elif self.hash_type == "sha256":
            hash = hashlib.sha256(word.encode()).hexdigest()
        return hash

    def reduce(self, hash, col):
        """
        hash: hash to reduce
        col: column number in hash
            Note: reduce method must be different for each column in rainbow table
        Returns a password reduced from a hash
        """
        pwd = ""
        int_reduce = int(hash, 16)
        while len(pwd) < self.password_max_size:
            pwd = pwd + self.chars[(int_reduce+col) % len(self.chars)]
            int_reduce = int_reduce // len(self.chars)
        return pwd

    def build_table(self):
        """
        Buils rainbow table by generating chain for each password of the list of passwords
        """
        for password in self.passwords:
            self.create_chain(password)

    def create_chain(self, pwd):
        """
        pwd: password to begin the chain with
        3 tables are important here
            - word table that contains every word that is being covered by this rainbow table
            - hash table is every hash that's being covered by this rainbowtable
            - rain table is a table containing the last hash of a chain
        """
        a = pwd
        self.word_table.append(a)
        for col in range(self.columns - 1):
            hash = self.hash_word(a)
            a = self.reduce(hash, col)
            self.word_table.append(a)
            self.hash_table.append(hash)
        hash = self.hash_word(a)
        self.rain_table.append(hash)
        self.hash_table.append(hash)

    def crack_hashed_pwd(self, start_hash):
        """ Tries to crack a hash by applying different reduce method to
            starting hash
        start_hash: hash to crack
        Returns the resulting password and null if not found

        """
        # starting crack at the end column of rainbow table and going over
        for col in range(self.columns, -1, -1):
            # find final hash of chain
            word_hash = self.get_last_hash(start_hash, col)
            # find password corresponding to final hash in rainbow table
            pwd_list = self._find(word_hash)
            # print('# col', col, "\n# word hash: ", word_hash, '\n# pwd_list: ', pwd_list)
            for pwd in pwd_list:
                result_password = self.find_hash_in_chain(pwd, start_hash)
                if result_password:
                    return result_password
        return 'Not found'

    def get_last_hash(self, start_hash, start_col):
        """ Finds the last hash of a sub chain
        start_hash: hash of beginning of sub chain
        start_col: column to begin chain
        Returns final hash of sub chain
        """
        word_hash = start_hash
        for col in range(start_col, self.columns - 1):
            pwd = self.reduce(word_hash, col)
            word_hash = self.hash_word(pwd)
        return word_hash

    def _find(self, word_hash):
        """
        word_hash: hash from which we want to find corresponding passwords
        Returns all the passwords corresponding to the hash
        """
        index_pwds = [index for index, item in enumerate(self.rain_table, 0)
                      if item == word_hash]
        pwds = [self.passwords[i] for i in index_pwds]
        return pwds

    def find_hash_in_chain(self, start_pwd, start_hash):
        """
        start_pwd: password in beginning of chain
        start_hash: hash of pwd to find
        Returns password if found
        """
        word_hash = self.hash_word(start_pwd)
        if word_hash == start_hash:
            return start_pwd
        col = 0
        while col < self.columns:
            pwd = self.reduce(word_hash, col)
            word_hash = self.hash_word(pwd)
            if word_hash == start_hash:
                return pwd
            col += 1
        return None

    def write_to_file(self):
        """
        writes down 2 different text files
            - rainbow table text file containing the table made of the first password and last hash of the chain
              and the number of password that are covered and tested and the success ratio of these test
            - textfile containing all the passwords covered in this rainbow table
        """
        open("RainbowTables\\rainbow_table-{}-{}.txt".format(self.password_max_size, self.rows), "w") \
            .write(json.dumps(
                {
                    "hashs": self.rain_table,
                    "pwds": self.passwords,
                    "n_password_tests": self.password_tested,
                    "success_ratio": self.success_ratio}))
        open("RainbowTables\\word_list-{}-{}.txt".format(self.password_max_size, self.rows), "w") \
            .write(json.dumps(
                {
                    "words": self.word_table
                }
            ))
        print("# RainbowTable created")

    def recover_rainbow_table(self, copy=0):
        """
        method to recover or not a rainbow table that's already been generated with same features
        (keep in mind that for now passwords are being randomly generated and thus never the same
        :param copy: possible argument if the user wants to do a copy of the file but not implemented for now
        :return: true if a rainbow table exists and false if not and thus a new rainbow table needs to be generated
        """
        if "rainbow_table-{}-{}.txt".format(self.password_max_size, self.rows) in os.listdir("RainbowTables"):
            dico = json.loads(open("RainbowTables\\rainbow_table-{}-{}.txt".format(self.password_max_size, self.rows), "r").read())
            self.rain_table = dico["hashs"]
            self.passwords = dico["pwds"]
            self.password_tested = dico["n_password_tests"]
            self.success_ratio = dico["success_ratio"]

            dico = json.loads(open("RainbowTables\\word_list-{}-{}.txt".format(self.password_max_size, self.rows), "r").read())
            self.word_table = dico["words"]

            # if copy == 1:
            #     self.hashs = []
            #     print("# listPwd generated")
            #     self.hashs = [self.hash(i) for i in self.listPwd]
            #     self.hashs = [self.computeHashChains(i) for i in self.hashs]
            #     open("RainbowTables\\copied{}.txt".format(self.n_character), "w") \
            #         .write(json.dumps({"hashs": self.hashs, "pwds": self.listPwd, "n_password_tests": -1, "ok": -1}))
            #     print("# RainbowTable copied")
            return True
        else:
            return False

    def test_collisions(self):
        """
        tests if rainbow table contains collisions and how many collision there are
        """
        test = len(self.hash_table) != len(set(self.hash_table))
        print("This table contains collisions : " + str(test))
        if test:
            self.collisions = len(self.hash_table)-len(set(self.hash_table))
            print("Total Collisions is :" + (str(self.collisions)))

    def test_rain(self):
        """
        Test how good rainbow table is working, meaning if rainbow table is able to crack a hash a password from word
        list
        for every word in the list, hashes the password and tries to crack it, if the returned password is equal to the
        initial password, means it worked and success count is incremented
        displays finally the results of the test
        """
        words_to_test = self.word_table
        count = 0
        for i, pwd in enumerate(words_to_test):
            hash = self.hash_word(pwd)
            if self.crack_hashed_pwd(hash) == pwd:
                print("success")
                count += 1
            if i % 100 == 0:
                print('Tested', i, '/', len(words_to_test), ':', count,
                      ' ', count / len(words_to_test))
        self.password_tested = count
        self.success_ratio = count / len(words_to_test) * 100
        print('Numbers of passwords successfully tested: ', count,
              '\nSucces ratio: ', self.success_ratio, '%')

    def test_rain_word_not_in_list(self):
        """
        method that shows that a password not in the list cannot be cracked
        """
        word = None
        ok = False
        while ok is False:
            word = self.password_generator()
            if word not in self.word_table:
                ok = True
        print("The word " + word + " was " + rain.crack_hashed_pwd(rain.hash_word(word)))

    def test_rain_with_word_in_list(self):
        """
        method that shows that any password in the word list can be cracked
        """
        word = random.choice(self.word_table)
        print("The word for the hash " + rain.hash_word(word) + " was " + rain.crack_hashed_pwd(rain.hash_word(word)))


# f = open("passwords.txt", "r")
# passwords = []
# for x in f:
#    password = "{}".format(x)
#    max = len(password)
#    passwords.append(password[:max-1])


# rain = RainbowGenerator(7, passwords)
rain = RainbowGenerator(7, 1000, hash_type="sha256")
rain.test_rain_word_not_in_list()
rain.test_rain_with_word_in_list()


