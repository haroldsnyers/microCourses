from passlib.hash import lmhash

f = open("passwords.txt", "r")
passwords = []
for x in f:
   password = "{}".format(x)
   max = len(password)
   passwords.append(password[:max-1])

print(passwords)

chars_ = "abcdefghijklmnopqrstuvwxyz"


class RainbowGenerator:
    def __init__(self, columns=0, list_passwords=None, chars=""):
        self.columns = columns
        self.passwords = list_passwords
        self.chars = chars
        self.rain_table, self.word_table, self.hash_table, self.hash_table_full = \
            self.build_table(self.passwords)

    @staticmethod
    def hash_word(word):
        """
        word: word to hash
        Returns the hashed word
        """
        return lmhash.hash(word)

    def reduce(self, hash, col):
        """
        hash: hash to reduce
        col: column number in hash
            Note: reduce method must be different for each column in rainbow table
        Returns a password reduced from a hash
        """
        pwd = ""
        int_reduce = int(hash, 16)
        while len(pwd) < 7:
            pwd = pwd + self.chars[(int_reduce+col) % len(self.chars)]
            int_reduce = int_reduce // len(self.chars)
        return pwd

    def build_table(self, list):
        """
        list: passwords list to make the rainbow table from
        Returns generated rainbow table and list of hashes and words that the
            rainbow table covers
        """
        rain_table = []
        word_table = []
        hash_table = []
        hash_table_full = []
        sObject = slice(self.columns)
        for password in list:
            chain, pwds, hashs = self.create_chain(password)
            rain_table.append(chain)
            word_table += pwds[sObject]
            hash_table_full += hashs[sObject]
            hash_table.append([chain[0], chain[-1]])
        return rain_table, word_table, hash_table, hash_table_full

    def _find(self, word_hash):
        """
        word_hash: hash from which we want to find corresponding passwords
        Returns all the passwords corresponding to the hash
        """
        index_pwds = [index for index, item in enumerate(self.hash_table, 0)
                      if item == word_hash]
        pwds = [self.word_table[i] for i in index_pwds]
        return pwds

    def create_chain(self, pwd):
        """
        pwd: password to begin the chain with
        Returns chain for each password given and returns a separate
            list of passwords and hashes contained in this chain
        """
        chain = [pwd]
        pwds = [pwd]
        hashs = []
        for col in range(self.columns):
            hash = self.hash_word(pwd)
            chain.append(hash)
            hashs.append(hash)
            if col != self.columns - 1:
                pwd = self.reduce(hash, col)
                chain.append(pwd)
                pwds.append(pwd)
        return chain, pwds, hashs

    def crack_hashed_pwd(self, start_hash):
        """ Tries to crack a hash by applying different reduce method to
            starting hash
        start_hash: hash to crack
        Returns the resulting password and null if not found

        """
        for col in range(self.columns, -1, -1):
            word_hash = self.get_last_hash(start_hash, col)
            pwd_list = self._find(word_hash)
            print('#col', col, "\n#word hash: ", word_hash, '\npwd_list: ', pwd_list)
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
        print(start_col)
        print(self.columns -1)
        for col in range(start_col, self.columns -1):
            pwd = self.reduce(word_hash, col)
            word_hash = self.hash_word(pwd)
        return word_hash

    def find_hash_in_chain(self, start_pwd, start_hash):
        """
        start_pwd
        start_hash: hash of pwd to find
        Returns password if found
        """
        print(start_pwd)
        print(start_hash)
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

    def write_to_file(self, file_path):
        f = open(file_path, 'w')
        data = [self.columns, self.chars]
        f.write(" ".join([str(i) for i in data]))
        f.write('\n')
        for x in self.rain_table:
            length = len(x)
            data = [x[0], x[length - 1]]
            f.write(" ".join(data))
            f.write('\n')

    def read_from_file(self, file_path):
        f = open(file_path, 'r')
        line = f.readline()
        line = line.strip().split(sep=" ")
        self.columns, self.chars = line
        self.columns = int(self.columns)


def test_rain(rain_table):
    """ Test how good rainbow table is working
rain_table : generated rainbow to test
    """
    count = 0
    for i, pwd in enumerate(passwords):
        hash = rain_table.hash_word(pwd)
        if rain_table.crack_hashed_pwd(hash) == pwd:
            count += 1
        if i % 10 == 0:
            print('Tested', i, '/', len(passwords), ':', count,
                  ' ', count / len(passwords))
    print('Numbers of passwords successfully tested: ', count,
          '\nSucces ratio: ', count / len(passwords) * 100, '%')


def test_collisions(rain_table):
    all_pwd = rain_table.word_table
    hashes = []
    count = 0
    for pwd in all_pwd:
        h = rain_table.hash_word(pwd)
        if h in hashes:
            count += 1
        hashes.append(h)
    print('Total collisions: ', count)


rain = RainbowGenerator(7, passwords, chars_)
# rain_table, word_table, hash_table = rain.build_table(passwords)

rain.write_to_file('rain_table.txt')
# rain.write_to_file(word_table, 'word_table.txt')
# rain.write_to_file(hash_table, 'hash_table.txt')

# test_rain(rain)
# test_collisions(rain)
# print(rain.crack_hashed_pwd(rain.hash_word('password')))
print(rain.crack_hashed_pwd(rain.hash_word('jmzoju')))
# print(rain.crack_hashed_pwd(rain.hash_word('qwerty')))
