fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())

## Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
def count_vowels(numbers):
    count = 0
    vowel = set('aeiouAEIOU')
    for number in numbers:
        if number in vowel:
            count += 1
    return count

fruits_with_more_than_two_vowels = [fruit for fruit in fruits if count_vowels(fruit)>2]
print(fruits_with_more_than_two_vowels)

#   ryan's solution
[fruit for fruit in fruits if
    (fruit.count('a') + fruit.count('e') fruit.count('i') fruit.count('o') fruit.count('u')) > 2]

def count_vowel2(fruit):
    fruit = fruit.lower()
    return fruit.count('a') + fruit.count('e') fruit.count('i') fruit.count('o') fruit.count('u')) > 2

[fruit for fruit in fruits if count_vowels2(fruit) > 2]

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
fruits_with_only_two_vowels = [fruit for fruit in fruits if count_vowels(fruit)==2]
print(fruits_with_only_two_vowels)

# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruits_with_more_than_5_characters = [fruit for fruit in fruits if len(fruit)>5]
print(fruits_with_more_than_5_characters)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruits_with_exactly_5_characters = [fruit for fruit in fruits if len(fruit)==5]
print(fruits_with_exactly_5_characters)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruits_with_less_than_5_characters = [fruit for fruit in fruits if len(fruit)<5]
print(fruits_with_less_than_5_characters)

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
number_of_characters_in_each_fruit = [len(fruit) for fruit in fruits]
print(number_of_characters_in_each_fruit)

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]
print(fruits_with_letter_a)

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [number for number in numbers if number % 2 == 1]
print(odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [number for number in numbers if number > 0]
print(positive_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [number for number in numbers if number < 0]
print(negative_numbers)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
numbers_with_2_or_more_numerals = [number for number in numbers if number >= 10 or number <= -10]
print(numbers_with_2_or_more_numerals)

# other solutions
[number for number in numbers if abs(number) >= 10]

[number for number in numbers if len(str(abs(number))) >= 2]

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = [number*number for number in numbers]
print(numbers_squared)

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [number for number in numbers if number < 0 and number % 2 != 0]
print(odd_negative_numbers)

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = [number + 5 for number in numbers]
print(numbers_plus_5)

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
primes = [number for number in numbers if number > 0 and all(number % y !=0 for y in range(2,number))]
print(primes)






