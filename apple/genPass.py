#  This is exclusively for generation of md5 hashes of Apple requirements for passwords 

import subprocess
import random
import string
import hashlib

i = 0
length = input("length: ")
hashAlg = raw_input("hashing algorithm: ")

while i < 1000:
    randomArr = []

    for x in range(0,length):
        randomArr.append(random.choice(string.ascii_lowercase))

    rInt = 0
    rUpper = 0
    rSymbol = 0

    while rInt == rUpper:
        rInt = random.randint(0,7)
        rUpper = random.randint(0,7)
        rSymbol = random.randint(0,7)
    
    randomArr[rInt] = str(random.randint(0,9))
    randomArr[rUpper] = random.choice(string.ascii_uppercase)
    randomArr[rSymbol] = random.choice(string.punctuation)
    #  simply changing the "hashlib.md5" to another hash algo will allow it to gen other possibilities 

    if hashAlg == "SHA256":
        #print(hashlib.sha256(str(''.join(randomArr))).hexdigest())
        print(str(''.join(randomArr)))

    if hashAlg == "MD5":
        #print(hashlib.md5(str(''.join(randomArr))).hexdigest())
        print(str(''.join(randomArr)))

    i += 1
