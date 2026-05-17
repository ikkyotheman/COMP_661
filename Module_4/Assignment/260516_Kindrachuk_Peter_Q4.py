fname = input('Enter the file name: ')
try:
    fhand = open(fname)
    for line in fhand:
        print(line, end='')
except:
    print('File cannot be opened:', fname)
    exit()