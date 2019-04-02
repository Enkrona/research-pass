#  This is exclusively for generation of md5 hashes of Apple requirements for passwords 

import subprocess
import random
import string
import hashlib
import uuid

i = 0
length = input()
hashAlg = raw_input()

def saltedSHA256(text):
    salt = ''
    for i in range(0,32):
        salt += random.choice(''.join((string.ascii_letters + string.digits)))
    return hashlib.sha256(salt + text).hexdigest() + ':' + salt

while i < 1000:
    randomArr = []

    for x in range(0,length):
        randomArr.append(random.choice(string.ascii_lowercase))

    rInt = 0
    rUpper = 0
    rSymbol = 0

    while rInt == rUpper:
        rInt = random.randint(0,length-1)
        rUpper = random.randint(0,length-1)
        #rSymbol = random.randint(0,length-1)

    randomArr[rInt] = str(random.randint(0,9))
    randomArr[rUpper] = random.choice(string.ascii_uppercase)
    #randomArr[rSymbol] = random.choice(string.punctuation)

    if hashAlg == "SHA256":
        print(hashlib.sha256(str(''.join(randomArr))).hexdigest())
    elif hashAlg == "MD5":
        print(hashlib.md5(str(''.join(randomArr))).hexdigest())
    elif hashAlg == "SHA256Salt":
	print(saltedSHA256(str(''.join(randomArr))))
    else:
        print(str(''.join(randomArr)))
    i += 1
