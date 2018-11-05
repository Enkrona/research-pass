import subprocess

pattern = ["?l","?l","?l","?l","?l","?l","?l"]
for x in range(0, 7):
    command = "echo hashcat --force --session " + str(x) + " -a3 hash.txt "
    pattern[x] = "?d"
    if x > 0:
        pattern [x-1] = "?l"

    tmp = ''.join(pattern)
    command += tmp
    subprocess.Popen(command, shell=True)
