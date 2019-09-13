# 4.3_control_structures_exercises.py

# Do your work for this exercise in a file named 4.3_control_structures_exercises.py.

# 1. Conditional Basics
#   a. prompt the user for a day of the week, print out whether the day is Monday or not
day_of_the_week = input("What is the day of the week? ")
if day_of_the_week in ["Monday", "Mon", "M"]:
    print("Today is Monday")
else:
    print("Today is not Monday")

#   b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day_of_the_week = input("What is the day of the week? ")
if day_of_the_week in ["Saturday", "Sunday"}:
    print("Today is a weekend")
else:
    print("Today is a weekday")

#   c. create variables and make up values for
#       the number of hours worked in one week
number_of_hours_worked_in_one_week = 40

#       the hourly rate
hourly_rate = 20

#       how much the week's paycheck will be
weeks_paycheck = number_of_hours_worked_in_one_week * hourly_rate
print(weeks_paycheck)
800
#       write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
weeks_paycheck = number_of_hours_worked_in_one_week * hourly_rate

def weekly_paycheck(number_of_hours_worked_in_one_week):
    hourly_rate = 20
    overtime_hours = 0
    overtime_pay = 1.5 * hourly_rate
    weeks_paycheck = number_of_hours_worked_in_one_week * hourly_rate
    if number_of_hours_worked_in_one_week > 40:
        overtime_hours = number_of_hours_worked_in_one_week - 40
        return (overtime_hours * (overtime_pay)
    else:
        return number_of_hours_worked_in_one_week * hourly_rate
# Davids example

if num_hours<=40:
    paycheck=num_hours*hour_wage
    print(paycheck)
else:
    paycheck=(num_hours-40)*1.5*hour_wage+40*hour_wage
    print("The weeks paycheck will be: "+str(paycheck))

# 2. Loop Basics

#   a. While
#       Create an integer variable i with a value of 5.
i = 5

#       Create a while loop that runs so long as i is less than or equal to 15
while i <= 15:
    print(i)
    
#       Each loop iteration, output the current value of i, then increment i by one.
while i <= 15:
    print(i)
    i += 1

#       Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i < 100:
    print(i)
    i += 2

for i in range(0,102,2):
    print(i)

#       Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i > -10:
    print(i)
    i -= 5

for i in range(100,-10,5):
    print(i)

#       Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
i = 2
while i**2 < 1_000_000:
    print(i**2)
    i = i**2

i = 2
while i<1000000:
    print(i)
    i = i ** 2
    

#       Write a loop that uses print to create the output shown below.
i = 100
while i > 5:
    print(i)
    i -= 5

for i in range(100,0,-5):
    print(i)


#   b. For Loops
#       i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
number = int(input("Enter one number greater than 0 and less than or equal to 10: "))
if number <= 10:
    print (f'{number} * 1 =', number * 1)
    print (f'{number} * 2 =', number * 2)
    print (f'{number} * 3 =', number * 3)
    print (f'{number} * 4 =', number * 4)
    print (f'{number} * 5 =', number * 5)
    print (f'{number} * 6 =', number * 6)
    print (f'{number} * 7 =', number * 7)
    print (f'{number} * 8 =', number * 8)
    print (f'{number} * 9 =', number * 9)
    print (f'{number} * 10 =', number * 10) 

else:
    print("You didn't follow the rules")

num = input("Enter a number")
num = int(num)
for i in range(1,11):
    print(str(i)+"*"+str(num)+"="+str(i*num))

#       ii. Create a for loop that uses print to create the output shown below.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    number = str(number) * number
    print(number)

for num in range(1,10):
    print
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

#   c. break and continue
#       i. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue 
#          prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this).
#          Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
number = input("Enter an odd number between 1 and 50: ")
while number in range()

    print(f'Here is an odder number: ')

    print(number)


odd_num = ""
while True:
    odd_num = input("enter an odd number between 1 and 50: ")
    if odd_num.isdigit() and int(odd_num)%2==1 and int(odd_num)>1 and int(odd_num)<50:
        break
for i in range(1,50,2):
    if i==int(odd_num):
        print("Yikes! Skipping number: "+str(i))
        continue
    print("Here is an odd number: "+str(i))

# Your output should look like this:


# Number to skip is: 27

# Here is an odd number: 1
# Here is an odd number: 3
# Here is an odd number: 5
# Here is an odd number: 7
# Here is an odd number: 9
# Here is an odd number: 11
# Here is an odd number: 13
# Here is an odd number: 15
# Here is an odd number: 17
# Here is an odd number: 19
# Here is an odd number: 21
# Here is an odd number: 23
# Here is an odd number: 25
# Yikes! Skipping number: 27
# Here is an odd number: 29
# Here is an odd number: 31
# Here is an odd number: 33
# Here is an odd number: 35
# Here is an odd number: 37
# Here is an odd number: 39
# Here is an odd number: 41
# Here is an odd number: 43
# Here is an odd number: 45
# Here is an odd number: 47
# Here is an odd number: 49

#   d. The input function can be used to prompt for input and use that input in your python code. 
#   Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
#   (Hints: first make sure that the value the user entered is a valid number, also note that the 
#   input function returns a string, so you'll need to convert this to a numeric type.)

pos_num = ""

if num_hours<=40:
    paycheck=num_hours*hour_wage
    print(paycheck)
else:
    paycheck=(num_hours-40)*1.5*hour_wage+40*hour_wage
    print("The weeks paycheck will be: "+str(paycheck))

#   e. Write a program that prompts the user for a positive integer. Next write a loop that prints
#   out the numbers from the number the user entered down to 1.
while True:
    pos_num=input("Please enter a positive number")
    if pos_num.isdigit() and int(pos_num)>0:
        break
for i in range(int(pos_num),0,-1):
    print(i)

# 3. Fizzbuzz

#   One of the most common interview questions for entry-level programmers is the FizzBuzz test.
#   Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

#   Write a program that prints the numbers from 1 to 100.
#   For multiples of three print "Fizz" instead of the number
#   For the multiples of five print "Buzz".
#   For numbers which are multiples of both three and five print "FizzBuzz".
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)



# 4. Display a table of powers.

#   Prompt the user to enter an integer.
#   Display a table of squares and cubes from 1 to the value entered.
#   Ask if the user wants to continue.
#   Assume that the user will enter valid data.
#   Only continue if the user agrees to.
while True:
    num_test=int(input("Please enter an integer"))
    for i in range(1,num_test+1):
        if i==1:
            print('number  | squared  | cubed')
            print('______  |  ______  |  ______')
    print(i,'  |', i**2,'  |',i**3)
    user_choice=input("Should we continue ?")
    if user_choice="no":
        break



# Example Output
# What number would you like to go up to? 5

# Here is your table!

# number | squared | cubed
# ------ | ------- | -----
# 1      | 1       | 1
# 2      | 4       | 8
# 3      | 9       | 27
# 4      | 16      | 64
# 5      | 25      | 125

# Bonus: Research python's format string specifiers to align the table

# 5. Convert given number grades into letter grades.
while True:
    num_grade=input("Please enter a grade between 0 and 100")
    num_grade=int(num_grade)
    if num_grade>=90:
        print('A')
    elif num_grade>=80:
        print('B')
    elif num_grade>=70:
        print('C')
    elif num_grade>=60:
        print('D') 
    else:
        print('F')
    prompt_user_continue=input("Would you like to continue? Y/N") 
    if prompt_user_continue.upper()=="N":
        break

#   Prompt the user for a numerical grade from 0 to 100.
#   Display the corresponding letter grade.
#   Prompt the user to continue.
#   Assume that the user will enter valid integers for the grades.
#   The application should only continue if the user agrees to.
#   Grade Ranges:

#       A : 100 - 88
#       B : 87 - 80
#       C : 79 - 67
#       D : 66 - 60
#       F : 59 - 0
# Bonus
# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

# 6. Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.

#   a. Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

def add_one(x):
    return x + 1


