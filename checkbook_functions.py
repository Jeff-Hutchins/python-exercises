

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

withdraw(20)

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

