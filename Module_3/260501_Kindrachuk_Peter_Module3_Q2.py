

piper = 'Peter Piper picked a peck of pickled peppers A peck of pickled peppers \
Peter Piper picked if Peter Piper picked a peck of pickled peppers Where is\
 the peck of pickled peppers Peter Piper picked'
dups = dict()
piper = piper.lower()
piper = piper.rstrip()
words = piper.split()

for word in words:
    if word not in dups:
        dups[word] = 1
    else:
        dups[word] += 1

print(sorted(dups.items()))