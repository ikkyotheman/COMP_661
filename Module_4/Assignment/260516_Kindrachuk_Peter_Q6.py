import os

with open('accounts.txt') as file:
    contents = file.read()

# update the name 'Zoltar' to 'Robert'
contents = contents.replace('Zoltar', 'Robert')

# create a tempfile with the new data
with open('tempfile.txt', 'w') as temp:
    temp.write(contents)

# Remove the original accounts.txt
os.remove('accounts.txt')

# Rename tempfile to myaccounts.txt
os.rename('tempfile.txt', 'myaccounts.txt')