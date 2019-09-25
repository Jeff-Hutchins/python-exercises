# Make a file named pandas_series.py or pandas_series.ipynb for the following exercises.

# Use pandas to create a Series from the following data:
import pandas as pd
import numpy as np

fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
# Name the variable that holds the series fruits.

fruits = pd.Series(fruits)
print(fruits)

# Run .describe() on the series to see what describe returns for a series of strings.

fruits.describe()

# Run the code necessary to produce only the unique fruit names.

fruits.unique()

# Determine how many times each value occurs in the series.

fruits.value_counts()

# Determine the most frequently occurring fruit name from the series.

fruits.value_counts().idxmax()

fruits.mode()

# Determine the least frequently occurring fruit name from the series.

least_frequent = fruits.value_counts().min()
frequencies = fruits.value_counts()
frequencies[frequencies == least_frequent]

# Write the code to get the longest string from the fruits series.

length_of_longest_string = fruits.str.len().max()
index_of_longest_string = fruits.str.len().idxmax()
longest_string = fruits[index_of_longest_string]

print("The longest string in the list of fruits is", longest_string, "and it has", length_of_longest_string)

# Find the fruit(s) with 5 or more letters in the name.

fruits[fruits.str.len() >= 5]

fruits[fruits.apply(lambda x: len(x) >= 5)]

# Capitalize all the fruit strings in the series.

fruits.str.capitalize()

# Count the letter "a" in all the fruits (use string vectorization)

counts_of_a = fruits.str.count("a")
list(zip(fruits, counts_of_a))    

# Output the number of vowels in each and every fruit.
def count_vowels(word):
    count = 0
    for letter in word:
        if letter in "aeiou":
            count += 1
    return count

fruits.apply(count_vowels)


# Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" 
# letters in the name.

fruits[fruits.apply(lambda x: x.count('o'))>1]
fruits

# Write the code to get only the fruits containing "berry" in the name

fruits[fruits.str.find('berry')>-1]

# Write the code to get only the fruits containing "apple" in the name

fruits[fruits.str.find('apple')>-1]

# Which fruit has the highest amount of vowels?

fruits[fruits.apply(count_vowels).max()]

# Use pandas to create a Series from the following data:
dollars = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

# What is the data type of the series?

type(dollars)
    # pandas.core.series.Series

# Use series operations to convert the series to a numeric data type.

dollars = dollars.str.replace('$',' ').str.strip().str.replace(',','_').str.replace('.','_').astype(int)
dollars

# What is the maximum value? The minimum?

dollars.max()
dollars.min()

# Bin the data into 4 equally sized intervals and show how many values fall into each bin.

pd.cut(dollars, 4).value_counts()

# Plot a histogram of the data. Be sure to include a title and axis labels.

pd.cut(dollars, 4).value_counts().hist()

# Use pandas to create a Series from the following exam scores:

exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

# What is the minimum exam score? The max, mean, median?

exam_scores
exam_scores.max()
exam_scores.mean()
exam_scores.median()

# Plot a histogram of the scores.

exam_scores.hist()

# Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' 
# and 95 should be an 'A'.

pd.cut(exam_scores, [0, 70, 80, 90, 100], labels=['F','C','B','A'])

# Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted 
# to a 100, and that many points should be given to every other score as well.

exam_scores + [100 - exam_scores.max()]

# Use pandas to create a Series from the following string:
string = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))
string
# What is the most frequently occuring letter? Least frequently occuring?

string[string.value_counts().max()]

# How many vowels are in the list?

string.apply(count_vowels)

# How many consonants are in the list?

def count_consonants(word):
    count = 0
    for letter in word:
        if letter not in "aeiou":
            count += 1
    return count

string.apply(count_consonants)

# Create a series that has all of the same letters, but uppercased

string.str.upper()

# Create a bar plot of the frequencies of the 6 most frequently occuring letters.

string.value_counts().head(6).plot.bar()
