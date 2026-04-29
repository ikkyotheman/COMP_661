import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t' ,'u', 'v', 'w', 'y', 'x', 'z']
i = 0
alpha = []
unique = []
while i < 10:
    letter = random.choice(alphabet)
    alpha.append(letter)
    if letter not in unique:
        unique.append(letter)
    i += 1
print('Random Letters')
print(alpha)
alpha_sorted = sorted(alpha)
print('Sort the list in ascending order.')
print(alpha_sorted)
alpha_sorted.reverse()
print('Sort the list in descending order.')
print(alpha_sorted)
print('Unique values sorted in as ascending order.')
unique.sort()
print(unique)