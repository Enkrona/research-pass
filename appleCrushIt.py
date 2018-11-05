import subprocess
def patternReset(pattern):
    for x in range (0, 8):
        pattern[x] = "?l"
    return pattern;

pattern = ["?l","?l","?l","?l","?l","?l","?l","?l"]

for x in range(0, 8):
    for y in range(0, 8):
        pattern = patternReset(pattern)
        pattern[x] = "?u"

        command = " echo hashcat --force --session " + str(x) + str(y) + " -a3 hash.txt "
        if pattern[y] != "?u":
            pattern[y] = "?d"


            tmp = ''.join(pattern)
            command += tmp
            subprocess.Popen(command, shell=True)
