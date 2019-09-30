# Take the word EASY: Its first three letters — E, A and S — are the fifth, first, and 
# nineteenth letters, respectively, in the alphabet. If you add 5, 1, and 19, you get 25, 
# which is the value of the alphabetical position of Y, the last letter of EASY.

# Can you think of a common five-letter word that works in the opposite way — in which 
# the value of the alphabetical positions of its last four letters add up to the value of 
# the alphabetical position of its first letter?

# Write some python code to solve the question above. You can find a list of words on your 
# mac at /usr/share/dict/words.

import pandas as pd
import numpy as np

with open('/usr/share/dict/words') as f:
    words = f.read().strip().split('\n')

print(f'There are {len(words):,} words.')
print(words[20000:20005])

# indexed the alphabet from 1 to 26 instead of 0 to 25.

# def sum_last_4_letters(i):
#     alphabet = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
#     alphabet.index = alphabet.index + 1
#     for word in words:
#         if len(word) === 5 and int

# for word in words:
#     if len(word) == 5 and :
#         print(word)

# need to the sum of the last 4 letters to equal the index value of the first letter.

five_letter_words = [w for w in words if len(w) == 5]

def alphabetical_position(c):
    return 'abcdefghijklmnopqrstuvwxyz'.index(c.lower()) + 1
def alphabetical_value(letters):
    return sum([alphabetical_position(c) for c in letters])

alphabetical_position('a')
alphabetical_value('ab')

for word in five_letter_words:
    # first_letter, *last_four_letters = word
    first_letter = word[0]
    last_four_letters = word[1:]
    if alphabetical_value(first_letter) == alphabetical_value(last_four_letters):
        print(word)

# Doing problem with Pandas

import pandas as pd

df = pd.DataFrame({'word': words})
df.head()

df.word.apply(len) == 5

# just the 5 letter words
df = df[df.word.apply(len) == 5]
df.head()

df['first_letter'] = df.word.str[0]
df['last_four'] = df.word.str[1:]
df

df['first_letter_val'] = df.first_letter.apply(alphabetical_position)
df['last_4_val'] = df.last_four.apply(alphabetical_value)
df

df[df.first_letter_val == df.last_4_val].word






