import subprocess

pattern = ["?l","?l","?l","?l","?l","?l","?l"]
for x in range(0, 7):
    command = "echo \"hashct -a3 hash.txt "
    pattern[x] = "?d"
    if x > 0:
        pattern [x-1] = "?l"

    tmp = ''.join(pattern)
    command += tmp
    command += "\""
    subprocess.Popen(command, shell=True)
