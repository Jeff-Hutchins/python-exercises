checkbook = [{"Balance": 100.00}]
print(checkbook[0]["Balance"])


welcome = "~~~ Welcome to your terminal checkbook! ~~~"

print(welcome)
print("                          ")
print("What would you like to do?")
print("                          ")
print("1) view current balance")
print("2) record a debit (withdraw)")
print("3) record a credit (deposit)")
print("4) exit")
print("                          ")
choice = input("Your choice? ")
debit = input("How much would you like to withdraw? ")
credit = input("How much would you like to deposit? ")
bye = "Have a great day!"

def loop(choice):
    if choice == 1:
        return current_balance
    elif choice == 2:
        return withdraw
    elif choice == 3:
        return deposit
    elif choice == 4:
        return bye
    else:
        return f"Invalid choice: {i}"


def current_balance(i):
    return checkbook[0]["Balance"]

def withdraw(i):
    return current_balance -= i

def deposit(i):ß
    return current_balance += i