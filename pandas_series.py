# Make a file named pandas_series.py or pandas_series.ipynb for the following exercises.

# Use pandas to create a Series from the following data:
import pandas as pd

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

# Determine the least frequently occurring fruit name from the series.

fruits.value_counts().idxmin()

# Write the code to get the longest string from the fruits series.



# Find the fruit(s) with 5 or more letters in the name.

# Capitalize all the fruit strings in the series.

# Count the letter "a" in all the fruits (use string vectorization)

# Output the number of vowels in each and every fruit.

# Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.

# Write the code to get only the fruits containing "berry" in the name

# Write the code to get only the fruits containing "apple" in the name

# Which fruit has the highest amount of vowels?

# Use pandas to create a Series from the following data:


# ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
# What is the data type of the series?
# Use series operations to convert the series to a numeric data type.
# What is the maximum value? The minimum?
# Bin the data into 4 equally sized intervals and show how many values fall into each bin.
# Plot a histogram of the data. Be sure to include a title and axis labels.
# Use pandas to create a Series from the following exam scores:


# [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
# What is the minimum exam score? The max, mean, median?
# Plot a histogram of the scores.
# Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.
# Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, and that many points should be given to every other score as well.
# Use pandas to create a Series from the following string:


# 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
# What is the most frequently occuring letter? Least frequently occuring?
# How many vowels are in the list?
# How many consonants are in the list?
# Create a series that has all of the same letters, but uppercased
# Create a bar plot of the frequencies of the 6 most frequently occuring letters.