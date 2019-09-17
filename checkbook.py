

def current_balance():
    f = open("checkbook_storage.txt","r")
    contents = f.readlines()
    amt = 0
    for x in contents:
        x = float(x)
        amt = x + amt
    return amt
    f.close()


def withdraw(i):
    converted_i = (float(i))
    f = open ("checkbook_storage.txt", "a")
    f.write('\n')
    subtract = str((converted_i) *-1)
    f.write(subtract)
    f = open("checkbook_storage.txt","r")
    contents = f.readlines()
    amt = 0
    for x in contents:
        x = float(x)
        amt = x + amt
    print(amt)
    f.close()
    

def deposit(i):
    converted_i = (float(i))
    f = open ("checkbook_storage.txt", "a")
    f.write('\n')
    subtract = str(converted_i)
    f.write(subtract)
    f = open("checkbook_storage.txt","r")
    contents = f.readlines()
    amt = 0
    for x in contents:
        x = float(x)
        amt = x + amt
    print(amt)
    f.close()

welcome = "~~~ Welcome to your terminal checkbook! ~~~"
print(welcome)


# choice = input("Your choice? ")
# debit = input("How much would you like to withdraw? ")
# credit = input("How much would you like to deposit? ")
# bye = "Have a great day!"


while True:
    print(
        "What would you like to do? \n"
        "                           \n"
        "1) View current balance?\n"
        "2) Record a debit (withdraw)\n"
        "3) record a credit (deposit)\n"
        "4) exit\n"
    )
    choice = input("Your choice? ")
    if choice == '1':
        print(f'Current Balance: ${current_balance()}')
    elif choice == '2':
        debit = input(f'Enter amount you would like to withdraw: $')
        withdraw(debit)
    elif choice == '3':
        credit = input(f'Enter amount you would like to deposit: $')
        deposit(credit)
    elif choice == '4':
        print('bye')
        break
    else:
        print(f"Invalid choice: {i}")

