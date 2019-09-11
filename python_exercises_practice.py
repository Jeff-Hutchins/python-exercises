type(99.9)
type("False")
type(False)
type('0')
type(0)
type(True)
type('True')
type[{}] #list of dictionary
type{'a':[]} #dictionary
type(.1)

# What data type would best represent:

# A term or phrase typed into a search box?
# string

# If a user is logged in?
# boolean

# A discount amount to apply to a user's shopping cart?
# float

# Whether or not a coupon code is valid?
# boolean

# An email address typed into a registration form?
# string

# The price of a product?
# float

# A Matrix?
# list

# The email addresses collected from a registration form?
# tuple

# Information about applicants to Codeup's data science program?
# dictionary

# You have rented some movies for your kids: 
# The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), 
# and Hercules (1 day, you don't know yet if they're 
# going to like it). If price for a movie per day 
# is 3 dollars, how much will you have to pay?

# Exercise 1
the_little_mermaid_days = 3
brother_bear_days = 5
hercules_days = 1
price = 3
total_price = (the_little_mermaid_days + brother_bear_days + hercules_days) * price
print(total_price)

# Exercise 2
google_hourly_rate = 400
amazon_hourly_rate = 380
facebook_hourly_rate = 350

pay = (google_hourly_rate * 6) + (amazon_hourly_rate * 4) + (facebook_hourly_rate * 10)

print(pay)

# Exercise 3
class_has_space = True
schedule_works = False
student_can_be_enrolled = class_has_space and schedule_works
print(student_can_be_enrolled)

is_class_full = False
class_schedule_conflict = False
enroll_student != is_class_full and class_schedule_conflict

enrolled = 0

def(student):
    if is_class_full = False and class_schedule_conflict = False
    return enrolled += 1

# Exercise 4
is_premium_member = True
person_bought_more_than_two_items = False
offer_has_not_expired = True

offer_can_be_applied = offer_has_not_expired and (person_bought_more_than_two_items or is_premium_member)
print(offer_can_be_applied)

# Exercise 5
username = "codeup"
password - "notastrongpassword"

password_at_least_five_characters = len(password) >= 5
username_has_less_than_20_characters = len(username) <= 20
password_and_username_different = username != password

username_starts_or_ends_with_white_space = username[0} == " " or username[-1] == " "]
username_starts_or_ends_with_white_space = password[0} == " " or password[-1] == " "]


