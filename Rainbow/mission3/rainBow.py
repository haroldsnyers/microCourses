f = open("test.txt", "r")
passwords = []
for x in f:
   password = "{}".format(x)
   passwords.append(password[:7])

print(passwords)

class RainbowGenerator:
    def __init__(self, columns=0, chars="", pwdLength=0, func='', rows=1000):
        self.columns = columns