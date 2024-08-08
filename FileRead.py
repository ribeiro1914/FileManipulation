## Open a txt file containing NAME, AGE, PASSED OR FAILLED

file = open('inputFile.txt', 'r')

# only displays names that passed

for line in file:
    # file is split by "space"
    res = line.split()
    if res[2] == 'P':
        print(line)

#print(file.read())
file.close