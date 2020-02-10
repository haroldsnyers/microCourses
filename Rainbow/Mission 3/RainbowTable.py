from passlib.hash import lmhash

f = open("passwords.txt", "r")
passwords = []
for x in f:
   password = "{}".format(x)
   max = len(password)
   passwords.append(password[:max-1])

print(passwords)

chars = "abcdefghijklmnopqrstuvwxyz"
chars_len = len(chars)


class RainbowGenerator:
    def __init__(self, columns=0):
        self.columns = columns

    @staticmethod
    def hash_word(word):
        return lmhash.hash(word)

    @staticmethod
    def reduce(int, col):
        pwd = ""
        while len(pwd)<7:
            pwd = pwd + chars[(int+col)%chars_len]
            int = int // chars_len
        return pwd

    def build_table(self, list):
        rain_table = []
        word_table = []
        for password in list:
            chain, pwds = self.create_chain(password)
            print(chain)
            rain_table.append(chain)
            word_table.append(pwds)
        return rain_table, word_table

    def create_chain(self, pwd):
        chain = [pwd]
        pwds = [pwd]
        for col in range(self.columns):
            hash = self.hash_word(pwd)
            chain.append(hash)
            if col != self.columns - 1:
                word = self.reduce(int(hash, 16), col)
                chain.append(word)
                pwds.append(word)
        return chain, pwds

    def crack_hashed_pwd(self, start_hash):
        for col in range(self.columns):

    # TODO mplement method to get last password of chain
    def get_last_hash(self, start_hash, start_col):

    # TODO implement method able to find if hash is found in chain
    def find_hash_in_chain(self, ):

    def write_to_file(self, table, file_path):
        f = open(file_path, 'w')
        for x in table:
            print(x)
            data = [i for i in x]
            f.write(" ".join(data))
            f.write('\n')
        print("full table = {}".format(table))

    # TODO : implement if possible tree to save words
    def find_word(self, word):
        for x in


rain = RainbowGenerator(7)
rain_table, word_table = rain.build_table(passwords)

rain.write_to_file(rain_table, 'rain_table.txt')
rain.write_to_file(word_table, 'word_table.txt')
