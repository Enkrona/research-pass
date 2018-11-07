# research-pass
Research performed by myself, Daniel Favor, and Dr.'s Nathan Eloe and Scott Bell

.masks files are used as pattern lists 

hashcat -a3 appleHash.txt apple.masks 

This command will utilize hashcat to bruteforce all password hashes found within appleHash.txt using apple.masks as the patterns for generating vlaid passwords. Thereby, this will reduce the ammount of "junk" or impossible combinations which will never be valid, and only generate crack passwords which follow the minimum spec requirements which Apple has (and mirrored in apple.masks). 


TODO: 
@Enkrona Look into where hashcat stores "Restore points" for ability to recover work done, if something were to crash
@Enkrona Migrate files into a more logical organizational structure 
