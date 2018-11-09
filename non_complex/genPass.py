#  This is exclusively for generation of hashes of lowercaase letter password hashes with a length variable  

import subprocess
import random
import string
import hashlib
i = 0

length = input("length: ");

while i < 1000:
    randomArr = []

    for x in range(0,length):
        randomArr.append(random.choice(string.ascii_lowercase))
    #  simply changing the "hashlib.md5" to another hash algo will allow it to gen other possibilities 
    
    print(hashlib.sha256(str(''.join(randomArr))).hexdigest())
    #print(str(''.join(randomArr)))
    i += 1
