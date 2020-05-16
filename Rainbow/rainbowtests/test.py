# pour des mots de 5 lettres -> génération d'une Rainbow 7 reduction, 100 chains sur base de LM hash

from passlib.hash import lmhash


def reduc_one(hash):
    return ''.join(hash[:5])


def reduc_two(hash):
    return ''.join(hash[len(hash) - 20:len(hash) - 15])


def reduc_tree(hash):
    reduc = ""
    for x in hash:
        if len(reduc) < 5:
            if x.isnumeric() :
                reduc += str(int(x) % 5)
        else:
            return reduc


def reduc_four(hash):
    reduc = ""
    for x in hash[0:6]:
        if x.isalpha():
            reduc += x.upper()
        else:
            reduc += str(int(x) % 5)
    return reduc


def reduc_five(hash):
    reduc = ""
    for x in hash[0:5]:
        if x.isalpha():
            reduc += x.upper()
        else:
            reduc += str(int(x) + 3)
    return reduc


def reduc_six(hash):
    reduc = ""
    status = True
    for x in hash[:5]:
        if x.isalpha() and status:
            reduc += x.lower()
            status = False
        else:
            reduc += x.upper()
            status = True
    return reduc


def reduc_seven(hash):
    reduc = ""
    for x in hash:
        if len(reduc) < 5:
            if x.isalpha():
                reduc += x.upper()
        else:
            return reduc


def rebuild(pwd):
    chain = [pwd]

    chain.append(lmhash.hash(chain[0]))
    chain.append(reduc_one(chain[1]))

    chain.append(lmhash.hash(chain[2]))
    chain.append(reduc_two(chain[3]))

    chain.append(lmhash.hash(chain[4]))
    chain.append(reduc_tree(chain[5]))

    chain.append(lmhash.hash(chain[6]))
    chain.append(reduc_four(chain[7]))

    chain.append(lmhash.hash(chain[8]))
    chain.append(reduc_five(chain[9]))

    chain.append(lmhash.hash(chain[10]))
    chain.append(reduc_six(chain[11]))

    chain.append(lmhash.hash(chain[12]))
    chain.append(reduc_seven(chain[13]))

    chain.append(lmhash.hash(chain[14]))
    return chain


def RainbowGeneration(list):
    rainbowTable = []
    reducRainbow = []
    for pwd in list:
        chain = rebuild(pwd)
        rainbowTable.append(chain)
        reducRainbow.append((pwd, chain[len(chain)-1]))
    return rainbowTable, reducRainbow


def generateRainbowFromTable(table):
    rainbow = []
    for pwd in table:
        rainbow.append(rebuild(pwd[0]))
    return rainbow


def findPassword(table, hash):
    rainbow = generateRainbowFromTable(table)
    for chain in rainbow:
        for i in range(len(chain)):
            if chain[i] == hash:
                return chain[i-1]


list = ["didier", "password", "123456", "123456789", "12345678", "12345", "111111", "1234567", "sunshine", "qwerty",
        "iloveyou", "princess", "admin", "welcome", "666666", "abc123", "football", "123123", "monkey", "654321",
        "!@#$%^&*", "charlie", "aa123456", "donald", "password1", "qwerty123", "zxcvbnm", "121212", "bailey", "freedom",
        "shadow",
        "passw0rd", "baseball", "buster", "daniel", "hannah", "thomas", "summer", "george", "harley", "222222",
        "jessica", "ginger",
        "letmein", "abcdef", "solo", "jordan", "55555", "tigger", "joshua", "pepper", "sophie", "robert", "matthew",
        "12341234",
        "andrew", "lakers", "andrea", "1qaz2wsx", "starwars", "ferrari", "cheese", "computer", "corvette", "mercedes",
        "blahblah",
        "maverick", "hello", "nicole", "hunter", "amanda", "jennifer", "banana", "chelsea", "ranger", "trustno1",
        "merlin",
        "cookie", "ashley", "bandit", "killer", "aaaaaa", "1q2w3e", "zaq1zaq1", "hockey", "dallas", "whatever",
        "admin123", "pussy",
        "liverpool", "querty", "william", "soccer", "london", "biteme", "victor", "bruxelles", "azertyuiop",
        "ordinateur", "internet"]

full, reduc = RainbowGeneration(list)

print("full table = {}".format(full))
print("reduc table = {}".format(reduc))


print(findPassword(reduc, "a8c8971fdbc4172daad3b435b51404ee"))