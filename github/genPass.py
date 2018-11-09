#  This is exclusively for generation of md5 hashes of Apple requirements for passwords 

import subprocess
import random
import string
import hashlib
i = 0

while i < 1000:
    randomArr = []

    for x in range(0,7):
        randomArr.append(random.choice(string.ascii_lowercase))

    randomArr[random.randint(0,6)] = str(random.randint(0,9))

    #  simply changing the "hashlib.md5" to another hash algo will allow it to gen other possibilities 
    
    command = "echo " + hashlib.sha256(str(''.join(randomArr))).hexdigest()
    #command = "echo " + str(''.join(randomArr))
    subprocess.Popen(command, shell=True)
    i += 1
