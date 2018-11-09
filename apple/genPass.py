#  This is exclusively for generation of md5 hashes of Apple requirements for passwords 

import subprocess
import random
import string
import hashlib
i = 0

while i < 1000:
    randomArr = []

    for x in range(0,8):
        randomArr.append(random.choice(string.ascii_lowercase))

    rint = 0
    rupper = 0
    while rint == rupper:
        rint = random.randint(0,7)
        rupper = random.randint(0,7)

    randomArr[rint] = str(random.randint(0,9))
    randomArr[rupper] = random.choice(string.ascii_uppercase)
    
    #  simply changing the "hashlib.md5" to another hash algo will allow it to gen other possibilities 
    
    command = "echo " + hashlib.sha256(str(''.join(randomArr))).hexdigest()
    subprocess.Popen(command, shell=True)
    i += 1
