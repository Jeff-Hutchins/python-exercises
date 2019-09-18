# 4.5)_import_exercises

# 1. Import and test 3 of the functions from your functions exercise file.

# Your functions exercise are not currently in a file with a name that can be easily imported. Copy your functions exercise file and name the copy functions_exercises.py.

# Import each function in a different way:

# import the module and refer to the function with the . syntax
# use from to import the function directly
# use from and give the function a different name

import functions_exercises as f
f.get_letter_grade(91)

from functions_exercises import is_two
is_two('2')

from functions_exercises import is_two as t 
t('2')

# For the following exercises, read about and use the itertools module from the standard library
#  to help you solve the problem.

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
# How many different ways can you combine two of the letters from "abcd"?

A = ['a', 'b', 'c', 1, 2, 3]
import itertools as iter
print(list(iter.combinations(A, 2)))

#iter.combinations(('abcd', '123'))

B = ['a', 'b', 'c', 'd']
print(list(iter.combinations(B, 2)))

#iter.combinations('abcd', 2)

# Save this file as profiles.json inside of your exercises directory. Use the load function from 
# the json module to open this file, it will produce a list of dictionaries. Using this data, write
# some code that calculates and outputs the following information:

import json
import re
from collections import defaultdict, Count
with open(profiles.json)

load profiles.json
import json
with open('profiles.json', 'r') as d:
    array = json.load(d)
    
# Total number of users

# Number of active users

active_users = [profile['isActive'] for profile in profiles if profile['isActive']]
n_active_users = len(active_users)

# Number of inactive users

active_users = [profile['isActive'] for profile in profiles if not profile['isActive']]
n_active_users = len(active_users)

# Grand total of balances for all users
def handle_balance(s):
    return float(s[1:].replace(',', ''))
    
balances = [handle_balance(profile['balance']) for profile in profiles]

sum(balances)

# Average balance per user

sum(balances / len(balances))

# User with the lowest balance

user_with_the_lowest_balance = profiles[0]
for user in profiles[1:]:
    if handle_balance(user['balance']) < handle_balance(user_with_the_lowest_balance['balance']):
        user_with_the_lowest_balance = user

user_with_the_lowest_balanace

# User with the highest balance

user_with_the_highest_balance = profiles[0]
for user in profiles[1:]:
    if handle_balance(user['balance']) > handle_balance(user_with_the_highest_balance['balance']):
        user_with_the_highest_balance = user
# or

min(profiles, key = lambda profile: handle_balance(profile['balance']))

# or

def extract_balance(profile):
    return handle_balance(profile['balance'])

min(profiles, key=extract_balance)

# Most common favorite fruit

[profile['favoriteFruit'] for profile in profiles]

from collections import Counter

Counter([profile['favoriteFruit'] for profile in profiles])

# Least most common favorite fruit

fruit_counts = {}
for profile in profiles:
    fruit = profile['favoriteFruit']
    if fruit in fruit_counts:
        fruit_counts[fruit] += 1
    else:
        fruit_counts[fruit] = 1

# Total number of unread messages for all users

greetings = [profile['greeting'] for profile in profiles]

def extract_digits(s):
    return ''.join([c for c in s if c.isdigit()])

extract_digits('abc123def')

[etract_digits(greeting) for greeting in greetings]

n_unread_messages = [extract_digits(greeting) for greeting in greetings]
sum(n_unread_messages)





