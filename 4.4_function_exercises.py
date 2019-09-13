# 4.4_function_exercises

# 1. Define a function named is_two. It should accept one input and return True if the passed
# input is either the number or the string 2, False otherwise.
def is_two(x):
    if type(x) == str or type(x) == int:
        return True
    else:
        return False

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel,
# False otherwise.
def is_vowel(letter):
    vowel = set('aeiouAEIOU')
    if letter in vowel:
        return True
    return False

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(word):
    vowel = ["a","e","i","o","u"]
    return word.lower not in vowel 


# 4. Define a function that accepts a string that is a word. The function should capitalize the first
# letter of the word if the word starts with a consonant.
def capitalize_first_letter_if_consonant(word):
    vowel = set('aeiouAEIOU')
    if word[0] not in vowel:
        return word.capitalize()
    return word


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1)
# and the bill total, and return the amount to tip.
def calculate_tip(tip_percentage, bill_total):
    return tip_percentage * bill_total

calculate_tip(.2, 20.5)

# 6. Define a function named apply_discount. It should accept a original price, and a discount
# percentage, and return the price after the discount is applied.
def apply_discount(og_price, discount_percentage):
    return og_price * (1-discount_percentage)

apply_discount(100, .2)

# 7. Define a function named handle_commas. It should accept a string that is a number that contains
# commas in it as input, and return a number as output.
def handle_commas(number_string_with_commas):
    number_string_with_commas = number_string_with_commas.split(",")
    return "".join(number_string_with_commas)

handle_commas("100,000,000")

# 8. Define a function named get_letter_grade. It should accept a number and return the letter
# grade associated with that number (A-F).
def get_letter_grade(number):
    if number >= 90:
        return 'A'
    elif number >= 80:
        return 'B'
    elif number >= 67:
        return 'C'
    elif number >= 60:
        return 'D' 
    else:
        return 'F'

get_letter_grade(92)

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the
# vowels removed.
def remove_vowels(str):
    newstr = str
    vowel = set('aeiouAEIOU')
    for i in str:
        if i in vowel:
            newstr = newstr.replace(i, "")
    return newstr

remove_vowels("Jeff")

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#   anything that is not a valid python identifier should be removed
#   leading and trailing whitespace should be removed
#   everything should be lowercase
#   spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed
def normalize_name(string):
    #strip() lower() replace(" ", "_")
    return string.lower().strip('%').strip().replace(" ", "_")
normalize_name('% Completed')

# 11. Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]


# Bonus
# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27