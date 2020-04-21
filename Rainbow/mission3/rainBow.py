from passlib.hash import lmhash

f = open("passwords.txt", "r")
passwords = []
for x in f:
   password = "{}".format(x)
   max = len(password)
   passwords.append(password[:max])

print(passwords)

chars = "abcdefghijklmnopqrstuvwxyz"
chars_len = len(chars)

class RainbowGenerator:
    def __init__(self, columns=0, pwdLength=0, rows=0):
        self.columns = columns
        self.pwdLength = pwdLength
        self.rows = rows


    def hashWord(self, word):
        return lmhash.hash(word)

    def reduce_one(self, int):
        pwd = ""
        while len(pwd)<7:
            pwd = pwd + chars[int%chars_len]
            int = int // chars_len
        return pwd

    def buildTable(self, list):
        table = []
        print('hello')
        print(list)
        for password in list:
            chain = []
            # hash
            hash = self.hashWord(password)
            chain.append(password)
            chain.append(hash)
            chain.append(self.reduce_one(int(hash, 16)))
            print(chain)
            table.append(chain)
        return table


    # def crackHash(self, startHash):
    #     for col in range(self.columns):
    #
    # def

    def writeToFile(self):
        f = open('test.txt', 'w')
        table = self.buildTable(passwords)
        for x in table:
            print(x)
            data = [i for i in x]
            f.write(" ".join(data))
            f.write('\n')
        print("full table = {}".format(table))


rain = RainbowGenerator()
rain.writeToFile()
