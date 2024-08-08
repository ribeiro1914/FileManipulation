## Open a txt file containing NAME, AGE, PASSED OR FAILLED

file = open('inputFile.txt', 'r')
passFile = open('passFile.txt','w')
failFile = open('failFile.txt','w')

# save records with Passed param in passFile
# save records with Failed param in failFile

for line in file:
    # file is split by "space"
    res = line.split()
    if res[2] == 'P':
        passFile.write(line)
    else:
        failFile.write(line)

#print(file.read())
file.close
passFile.close
failFile.close