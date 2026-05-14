# inp = input('Enter a file to open: ')
# try:
#     fhand = open(inp)
# except:
#     print('File cannot be opened:', inp)
#     exit()
# count = 0
# for line in fhand:
#     count += 1
# print('There are ', count, 'lines in ', inp)
# fhand = fhand.read()
# print(fhand)
# fhand = fhand.rstrip()
# print(fhand)

servers = {
    'web-01' : {'status':'online','ip':'192.168.1.1' },
    'web-02' : {'status':'offline','ip':'192.168.1.0' },
    'web-03' : {'status':'online','ip':'192.168.1.3' },
}
for k, v in servers.items():
    print(f'{k} | {v}')