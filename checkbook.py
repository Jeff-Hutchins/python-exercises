# Starts with my 3 functions.  My while loop is below.

def current_balance():
    '''
    Pulls current balance from my checkboo_storage.txt file.
    '''
    f = open("checkbook_storage.txt","r")
    contents = f.readlines()
    amt = 0
    for x in contents:
        x = float(x)
        amt = x + amt
    return amt
    f.close()


def withdraw(i):
    '''
    Withdraws amount of money that is entered into the function and
    displays updated current balance.
    '''
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
    print(
        '\n'
        f'Current Balance: ${amt}'
        '\n'
        )
    f.close()
    

def deposit(i):
    '''
    Deposits amount of money entered into the function and
    displays updated current balance.
    '''
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
    print(
        '\n'
        f'Current Balance: ${amt}'
        '\n'
        )
    f.close()

# Accepts inputs 1-4.  Checks current balance, allows withdrawals, 
# allows deposits.  If any other number is chosen it says invalid choice
# then returns to the main menu.

while True:
    print(
        "\n"
        "~~~ Welcome to your terminal checkbook! ~~~\n"
        "\n"
        "What would you like to do? \n"
        "                           \n"
        "1) View current balance?\n"
        "2) Record a debit (withdraw)\n"
        "3) Record a credit (deposit)\n"
        "4) Exit\n"
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
        print(
            '\n'
            'Thanks! Have a nice Day.'
            '\n'
            )
        break
    else:
        print(
            '\n'
            'Invalid choice'
            '\n'
            )

