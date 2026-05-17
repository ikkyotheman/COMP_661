count = 0
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
    for word in fhand.read().split():
        if len(word) == 5:
            count += 1
    print(f'There are {count} five letter words in the file')
except:
    print('File cannot be opened:', fname)
    exit()