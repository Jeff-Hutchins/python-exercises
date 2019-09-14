# 4.4_function_exercises

# 1. Define a function named is_two. It should accept one input and return True if the passed
# input is either the number or the string 2, False otherwise.
def is_two(x):
    return x == 2 or x == '2'
    # return x in [2, '2']
assert is_two(2) == True
assert is_two('2') == True
assert is_two('four') == False
assert is_two(3) == False
is_two(1.5)

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel,
# False otherwise.
def is_vowel(letter):
    vowel = set('aeiouAEIOU')
    if letter in vowel:
        return True
    return False

is_vowel('a')

# Zach's
def is_vowel(c):
    return len(c) == 1 and c.lower() in 'aeiou'

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(word):
    # vowel = ["a","e","i","o","u"]
    # return len(word) == 1 word.lower not in vowel 
    return not is_vowel(word)
# Zach's


# 4. Define a function that accepts a string that is a word. The function should capitalize the first
# letter of the word if the word starts with a consonant.
def capitalize_first_letter_if_consonant(word):
    vowel = set('aeiouAEIOU')
    if word[0] not in vowel:
        return word.capitalize()
    return word
   
def capitalize_first_letter_if_consonant(word):   
    if is_consonant(word[0]):
        return word.capitalize()
    return word

# Zach's
def capitalize_first_letter_if_consonant(word):
    word.capitalize() if is_consonant(word[0]) else word

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1)
# and the bill total, and return the amount to tip.
def calculate_tip(tip_percentage, bill_total):
    if tip_percentage > 1:
        tip_percentage /= 100
    return tip_percentage * bill_total

assert calculate_tip(.2, 20) == 4.0
assert calculate_tip(.25, 80) == 4.0 
assert calculate_tip(25, 80) == 20.0

# 6. Define a function named apply_discount. It should accept a original price, and a discount
# percentage, and return the price after the discount is applied.
def apply_discount(og_price, discount_percentage):
    return og_price * (1-discount_percentage)

assert apply_discount(20, .1) == 18.0
assert apply_discount(100, .2) == 80.0
# 7. Define a function named handle_commas. It should accept a string that is a number that contains
# commas in it as input, and return a number as output.
def handle_commas(number_string_with_commas):
    number_string_with_commas = number_string_with_commas.split(",")
    return "".join(number_string_with_commas)
    
def handle_commas(s)   
    return float(s.replace(',', ''))

def handle_commas(s)   
    s = s.replace(',', '')
    return float(s)

def handle_commas(s) 
    return  float(''.join([c for c in s if c != ',']))

'a,b,c,d'.split(',')
list('abcde')



handle_commas("100,000,000")

# 8. Define a function named get_letter_grade. It should accept a number and return the letter
# grade associated with that number (A-F).
def get_letter_grade(number):
    if number >= 90:
        return 'A'
    elif number >= 80:
        return 'B'
    elif number >= 70:
        return 'C'
    elif number >= 60:
        return 'D' 
    else:
        return 'F'

# Zach's
grades = {
    'A': range(94, 101),
    'B': range(87, 94),
    'C': range(80, 87),
    'D': range(70, 80),
    'F': range(0, 70),

}
def get_letter_grade(grade):
    for grade_letter, grade_range in grades.items():
        if round(n) in grade_range:
            return grade_letter
    return 'Error: don\'t know how to get a letter grade for %s' % n

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
    for i in string:
        if not i.isidentifier():
            string = string.replace(i, " ")
    string = string.lower().strip('%').strip().replace(" ", "_") 
    return string

# 1st iteration >>>>>  return string.lower().strip('%').strip().replace(" ", "_") for i in stuff

normalize_name(' Completed')

# 11. Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]
def cumsum(list):
    for number in range(1, len(list)):
        list[number] = list[number] + sum(list[number-1:number])
    return list

cumsum([1,2,3,4])

# Bonus
# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm
# and return a string that is the representation of the time in a 24-hour format. 
def twelveto24(time):
    if time.endswith('pm') and not time.startswith('12'):
        time = str(int(time[:1]) + 12) + time[2:8]
        return time.strip('pm')
    else:
        return time.strip('am')

twelveto24('10:30pm')

# found online
def convert24(str1): 
      
    # Checking if last two elements of time 
    # is AM and first two elements are 12 
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2] 
          
    # remove the AM     
    elif str1[-2:] == "AM": 
        return str1[:-2] 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2] 
          
    else: 
          
        # add 12 to hours and remove PM 
        return str(int(str1[:2]) + 12) + str1[2:8] 
  
# Driver Code         
print(convert24("08:05:45 PM")) 
# Bonus write a function that does the opposite.


#Bonus
# Create a function named col_index. It should accept a spreadsheet column name, and return the
# index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27
def col_index(column_name):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    index = 0
    for i in range(1,len(column_name)+1):
        index += (alphabet.index(column_name[-i].lower())+1 )* (26 ** (i-1))
    return index

# Need to add one to each alphabet.index(i).lower in order to get correct number.

# col_index('BB')

# def insert_comma(string):
#     return string.split(",")

# print(insert_comma("abcdefghijklmnopqrstuvwxyz"))


# More Bonus
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# add x for y times
def multiply(x, y):
    product = 0
    for i in range(0, y):
        product += x
    return product

multiply(6, 7)


divide(80, 10)

def division(numerator,denominator):
    if denominator == 0:
        raise ZeroDivisionError
    fraction  = 0
    while numerator >= denominator:
          numerator = numerator - denominator
          fraction  = fraction + 1
    return fraction 

division(80, 10)