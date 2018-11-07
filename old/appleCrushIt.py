import subprocess
def patternReset(pattern):
    for x in range (0, 8):
        pattern[x] = "?l"
    return pattern;

pattern = ["?l","?l","?l","?l","?l","?l","?l","?l"]
sessionID = 0
for x in range(0, 8):
    for y in range(0, 8):
        pattern = patternReset(pattern)
        pattern[x] = "?u"

        if pattern[y] != "?u":
            pattern[y] = "?d"
	    sessionID += 1
	    command = " echo hashcat --force --session " + str(sessionID) + " -a3 hash.txt "

            tmp = ''.join(pattern)
            command += tmp
            subprocess.Popen(command, shell=True)
