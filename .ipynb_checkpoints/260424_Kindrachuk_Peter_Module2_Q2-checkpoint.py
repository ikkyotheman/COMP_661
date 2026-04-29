# Q2. Insert 10 random letters in the range ‘a’ through ‘z’ into a list. Perform the following tasks and display your results

# (Maybe a while loop
# i = 1
# i <= 10
# Random.choice [alphabet], )

# a. Sort the list in ascending order

# b. Sort the list in descending order

# **c. Get the unique values sort them in ascending order**

# **Console:**

# Random Letters  
# ['e', 'h', 'f', 'h', 'j', 'b', 'j', 'b', 'a', 'c']  
# Sort the list in ascending order.  
# ['a', 'b', 'b', 'c', 'e', 'f', 'h', 'h', 'j', 'j']  
# Sort the list in descending order.  
# [‘j’, 'j', 'h', 'h', 'f', 'e', 'c', 'b', 'b', 'a']  
# Unique values sorted in as ascending order.  
# ['a', 'b', 'c', 'e', 'f', 'h', 'j']


import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t' ,'u', 'v', 'w', 'y', 'x', 'z']
i = 0
alpha = []
while i < 10:
    letter = random.choice(alphabet)
    alpha.append(letter)
    i += 1
print(alpha)
alpha_sorted = sorted(alpha) 
print(alpha_sorted)
alpha_rev_slice = alpha_sorted[::-1] # If you feel like a slice reverse
print(alpha_rev_slice)
alpha_sorted.reverse()               # Using the 'reverse' method (returns 'None')
print(alpha_sorted)
